#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from geometry_msgs.msg import Twist, TransformStamped
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Range, Image, CameraInfo
from std_msgs.msg import String
import tf2_ros

import socket
import select
import threading
import json
import struct
import numpy as np
import cv2
from cv_bridge import CvBridge

class UnrealROSBridgeNode(Node):
    def __init__(self):
        super().__init__('unreal_ros_bridge')

        self.declare_parameter('host', '127.0.0.1')
        self.declare_parameter('port', 9876)
        self.host = self.get_parameter('host').value
        self.port = self.get_parameter('port').value

        self.cv_bridge = CvBridge()
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)

        # Publishers
        self.odom_pub = self.create_publisher(Odometry, '/odom', 10)
        self.image_pub = self.create_publisher(Image, '/camera/image_raw', 10)
        self.camera_info_pub = self.create_publisher(CameraInfo, '/camera/camera_info', 10)
        
        self.sonar_front_pub = self.create_publisher(Range, '/sensors/sonar_front', 10)
        self.sonar_left_pub = self.create_publisher(Range, '/sensors/sonar_left', 10)
        self.sonar_back_pub = self.create_publisher(Range, '/sensors/sonar_back', 10)
        self.sonar_right_pub = self.create_publisher(Range, '/sensors/sonar_right', 10)

        self.oled_pub = self.create_publisher(String, '/nodemcu/oled_status', 10)

        # Subscribers
        self.cmd_vel_sub = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10
        )

        self.latest_cmd_vel = {'vx': 0.0, 'wz': 0.0}
        self.client_socket = None
        self.running = True

        # Start TCP server thread
        self.server_thread = threading.Thread(target=self.run_tcp_server, daemon=True)
        self.server_thread.start()

        self.get_logger().info(f'Unreal-ROS2 Bridge Node initialized. Listening on {self.host}:{self.port}')

    def cmd_vel_callback(self, msg: Twist):
        self.latest_cmd_vel = {
            'vx': float(msg.linear.x),
            'wz': float(msg.angular.z)
        }
        if self.client_socket:
            try:
                cmd_bytes = json.dumps({'cmd_vel': self.latest_cmd_vel}).encode('utf-8')
                header = struct.pack('>I', len(cmd_bytes))
                self.client_socket.sendall(header + cmd_bytes)
            except Exception as e:
                self.get_logger().warn(f'Failed to send cmd_vel to Unreal: {e}')
                self.client_socket = None

    def run_tcp_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.host, self.port))
        server.listen(1)

        while self.running:
            try:
                self.get_logger().info('Waiting for Unreal Engine simulation connection...')
                client, addr = server.accept()
                self.get_logger().info(f'Connected to Unreal Engine at {addr}')
                self.client_socket = client
                self.handle_client(client)
            except Exception as e:
                if self.running:
                    self.get_logger().error(f'Server socket exception: {e}')

    def handle_client(self, client):
        buffer = bytearray()
        while self.running:
            try:
                # Read packet length header (4 bytes)
                data = client.recv(65536)
                if not data:
                    break
                buffer.extend(data)

                while len(buffer) >= 4:
                    payload_len = struct.unpack('>I', buffer[:4])[0]
                    if len(buffer) < 4 + payload_len:
                        break  # Wait for full payload

                    payload = bytes(buffer[4:4 + payload_len])
                    buffer = buffer[4 + payload_len:]
                    self.process_unreal_payload(payload)

            except Exception as e:
                self.get_logger().warn(f'Connection interrupted: {e}')
                break

        if self.client_socket == client:
            self.client_socket = None
        client.close()
        self.get_logger().info('Unreal Engine disconnected.')

    def process_unreal_payload(self, payload: bytes):
        try:
            # Check if binary camera frame or JSON telemetry
            if payload.startswith(b'IMG:'):
                # Format: IMG:timestamp:JPEG_DATA
                colon_idx = payload.find(b':', 4)
                img_data = payload[colon_idx + 1:]
                np_arr = np.frombuffer(img_data, np.uint8)
                cv_img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
                if cv_img is not None:
                    now = self.get_clock().now().to_msg()
                    ros_img = self.cv_bridge.cv2_to_imgmsg(cv_img, encoding='bgr8')
                    ros_img.header.stamp = now
                    ros_img.header.frame_id = 'camera_optical_link'
                    self.image_pub.publish(ros_img)

                    # Camera info
                    cam_info = CameraInfo()
                    cam_info.header = ros_img.header
                    cam_info.width = 1280
                    cam_info.height = 720
                    cam_info.distortion_model = 'plumb_bob'
                    f = 600.0
                    cam_info.k = [f, 0.0, 640.0, 0.0, f, 360.0, 0.0, 0.0, 1.0]
                    self.camera_info_pub.publish(cam_info)
                return

            packet = json.loads(payload.decode('utf-8'))
            now = self.get_clock().now().to_msg()

            # 1. Odometry & TF
            if 'odom' in packet:
                odom_data = packet['odom']
                x = odom_data.get('x', 0.0)
                y = odom_data.get('y', 0.0)
                yaw = odom_data.get('yaw', 0.0)
                vx = odom_data.get('vx', 0.0)
                wz = odom_data.get('wz', 0.0)

                # Broadcast TF: odom -> base_footprint
                t = TransformStamped()
                t.header.stamp = now
                t.header.frame_id = 'odom'
                t.child_frame_id = 'base_footprint'
                t.transform.translation.x = float(x)
                t.transform.translation.y = float(y)
                t.transform.translation.z = 0.0

                qz = np.sin(yaw / 2.0)
                qw = np.cos(yaw / 2.0)
                t.transform.rotation.z = float(qz)
                t.transform.rotation.w = float(qw)
                self.tf_broadcaster.sendTransform(t)

                # Publish /odom
                odom_msg = Odometry()
                odom_msg.header.stamp = now
                odom_msg.header.frame_id = 'odom'
                odom_msg.child_frame_id = 'base_footprint'
                odom_msg.pose.pose.position.x = float(x)
                odom_msg.pose.pose.position.y = float(y)
                odom_msg.pose.pose.orientation.z = float(qz)
                odom_msg.pose.pose.orientation.w = float(qw)
                odom_msg.twist.twist.linear.x = float(vx)
                odom_msg.twist.twist.angular.z = float(wz)
                self.odom_pub.publish(odom_msg)

            # 2. HC-SR04 Sonar Readings
            if 'sonars' in packet:
                sonars = packet['sonars']
                self.publish_sonar(self.sonar_front_pub, 'sonar_front_link', sonars.get('front', 4.0), now)
                self.publish_sonar(self.sonar_left_pub, 'sonar_left_link', sonars.get('left', 4.0), now)
                self.publish_sonar(self.sonar_back_pub, 'sonar_back_link', sonars.get('back', 4.0), now)
                self.publish_sonar(self.sonar_right_pub, 'sonar_right_link', sonars.get('right', 4.0), now)

            # 3. NodeMCU OLED status
            if 'oled' in packet:
                msg = String()
                msg.data = json.dumps(packet['oled'])
                self.oled_pub.publish(msg)

        except Exception as e:
            self.get_logger().error(f'Error processing Unreal payload: {e}')

    def publish_sonar(self, publisher, frame_id, distance_m, stamp):
        r = Range()
        r.header.stamp = stamp
        r.header.frame_id = frame_id
        r.radiation_type = Range.ULTRASOUND
        r.field_of_view = 0.523599  # 30 deg in radians
        r.min_range = 0.02
        r.max_range = 4.00
        r.range = float(np.clip(distance_m, 0.02, 4.00))
        publisher.publish(r)

    def destroy_node(self):
        self.running = False
        if self.client_socket:
            try:
                self.client_socket.close()
            except Exception:
                pass
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = UnrealROSBridgeNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
