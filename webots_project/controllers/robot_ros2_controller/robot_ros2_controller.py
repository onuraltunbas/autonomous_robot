#!/usr/bin/env python3
"""
Webots Native ROS 2 Robot Controller for 4WD Autonomous Box Robot
Handles 4WD Skid-Steer DC motors, 4x HC-SR04 sonars, 720p Camera, and OLED Display.
"""

import os
import sys
import math
import numpy as np

# Ensure Webots controller API can be imported
webots_home = os.environ.get('WEBOTS_HOME', '/home/onur/webots')
python_lib = os.path.join(webots_home, 'lib', 'controller', 'python')
if python_lib not in sys.path:
    sys.path.append(python_lib)

from controller import Robot, DistanceSensor, Camera, Display

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TransformStamped
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Range, Image, CameraInfo, JointState
from std_msgs.msg import String
import tf2_ros

class WebotsRobotROS2(Node):
    def __init__(self, robot, timestep):
        super().__init__('webots_robot_ros2')
        self.robot = robot
        self.timestep = timestep

        # Kinematic dimensions (20cm chassis, 6.5cm diameter wheels)
        self.wheel_radius = 0.0325
        self.track_width = 0.225
        self.wheelbase = 0.120

        # Physical state
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.linear_x = 0.0
        self.angular_z = 0.0

        # Setup Motors
        self.fl_motor = self.robot.getDevice('fl_motor')
        self.fr_motor = self.robot.getDevice('fr_motor')
        self.rl_motor = self.robot.getDevice('rl_motor')
        self.rr_motor = self.robot.getDevice('rr_motor')

        for m in [self.fl_motor, self.fr_motor, self.rl_motor, self.rr_motor]:
            if m:
                m.setPosition(float('inf'))
                m.setVelocity(0.0)

        # Setup 4x HC-SR04 DistanceSensors
        self.sonar_front = self.robot.getDevice('sonar_front')
        self.sonar_left  = self.robot.getDevice('sonar_left')
        self.sonar_back  = self.robot.getDevice('sonar_back')
        self.sonar_right = self.robot.getDevice('sonar_right')

        for s in [self.sonar_front, self.sonar_left, self.sonar_back, self.sonar_right]:
            if s:
                s.enable(self.timestep)

        # Setup 720p Camera
        self.camera = self.robot.getDevice('camera')
        if self.camera:
            self.camera.enable(self.timestep)

        # Setup OLED Display
        self.oled = self.robot.getDevice('oled_display')
        if self.oled:
            self.init_oled()

        # ROS 2 Publishers
        self.odom_pub = self.create_publisher(Odometry, '/odom', 10)
        self.sonar_front_pub = self.create_publisher(Range, '/sensors/sonar_front', 10)
        self.sonar_left_pub  = self.create_publisher(Range, '/sensors/sonar_left', 10)
        self.sonar_back_pub  = self.create_publisher(Range, '/sensors/sonar_back', 10)
        self.sonar_right_pub = self.create_publisher(Range, '/sensors/sonar_right', 10)
        self.image_pub = self.create_publisher(Image, '/camera/image_raw', 10)
        self.cam_info_pub = self.create_publisher(CameraInfo, '/camera/camera_info', 10)
        self.oled_pub = self.create_publisher(String, '/nodemcu/oled_status', 10)
        self.joint_pub = self.create_publisher(JointState, '/joint_states', 10)

        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)

        # ROS 2 Subscribers
        self.cmd_sub = self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)

        self.get_logger().info('Webots Autonomous Box Robot ROS 2 Controller Initialized!')

    def init_oled(self):
        self.oled.setColor(0x000000)
        self.oled.fillRectangle(0, 0, 128, 64)
        self.oled.setColor(0x00E5FF)
        self.oled.drawText("NodeMCU Active", 5, 5)

    def cmd_vel_callback(self, msg: Twist):
        self.linear_x = float(msg.linear.x)
        self.angular_z = float(msg.angular.z)

    def update_motors(self):
        # 4WD Skid-steer kinematics:
        # w_l = (vx - wz * (W/2)) / r
        # w_r = (vx + wz * (W/2)) / r
        w_left = (self.linear_x - self.angular_z * (self.track_width / 2.0)) / self.wheel_radius
        w_right = (self.linear_x + self.angular_z * (self.track_width / 2.0)) / self.wheel_radius

        # Clamp to motor limits
        max_v = 20.0
        w_left = max(-max_v, min(max_v, w_left))
        w_right = max(-max_v, min(max_v, w_right))

        if self.fl_motor: self.fl_motor.setVelocity(w_left)
        if self.rl_motor: self.rl_motor.setVelocity(w_left)
        if self.fr_motor: self.fr_motor.setVelocity(w_right)
        if self.rr_motor: self.rr_motor.setVelocity(w_right)

    def publish_sensors(self):
        now = self.get_clock().now().to_msg()
        dt = self.timestep / 1000.0

        # Integrate Odometry
        self.yaw += self.angular_z * dt
        self.x += self.linear_x * math.cos(self.yaw) * dt
        self.y += self.linear_x * math.sin(self.yaw) * dt

        # TF odom -> base_footprint
        t = TransformStamped()
        t.header.stamp = now
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_footprint'
        t.transform.translation.x = float(self.x)
        t.transform.translation.y = float(self.y)
        t.transform.translation.z = 0.0

        qz = math.sin(self.yaw / 2.0)
        qw = math.cos(self.yaw / 2.0)
        t.transform.rotation.z = float(qz)
        t.transform.rotation.w = float(qw)
        self.tf_broadcaster.sendTransform(t)

        # Odometry msg
        odom = Odometry()
        odom.header.stamp = now
        odom.header.frame_id = 'odom'
        odom.child_frame_id = 'base_footprint'
        odom.pose.pose.position.x = float(self.x)
        odom.pose.pose.position.y = float(self.y)
        odom.pose.pose.orientation.z = float(qz)
        odom.pose.pose.orientation.w = float(qw)
        odom.twist.twist.linear.x = float(self.linear_x)
        odom.twist.twist.angular.z = float(self.angular_z)
        self.odom_pub.publish(odom)

        # Publish 4x HC-SR04 Range Sensors
        def get_dist(sensor):
            if sensor:
                val = sensor.getValue()
                return max(0.02, min(4.00, float(val)))
            return 4.00

        d_front = get_dist(self.sonar_front)
        d_left  = get_dist(self.sonar_left)
        d_back  = get_dist(self.sonar_back)
        d_right = get_dist(self.sonar_right)

        def make_range(frame_id, dist):
            r = Range()
            r.header.stamp = now
            r.header.frame_id = frame_id
            r.radiation_type = Range.ULTRASOUND
            r.field_of_view = 0.52
            r.min_range = 0.02
            r.max_range = 4.00
            r.range = float(dist)
            return r

        self.sonar_front_pub.publish(make_range('sonar_front_link', d_front))
        self.sonar_left_pub.publish(make_range('sonar_left_link', d_left))
        self.sonar_back_pub.publish(make_range('sonar_back_link', d_back))
        self.sonar_right_pub.publish(make_range('sonar_right_link', d_right))

        # Publish Camera frame if ready
        if self.camera:
            img_data = self.camera.getImage()
            if img_data:
                msg = Image()
                msg.header.stamp = now
                msg.header.frame_id = 'camera_optical_link'
                msg.height = self.camera.getHeight()
                msg.width = self.camera.getWidth()
                msg.encoding = 'bgra8'
                msg.is_bigendian = 0
                msg.step = msg.width * 4
                msg.data = list(img_data)
                self.image_pub.publish(msg)

        # OLED Display Update (every 200ms)
        f_cm = int(d_front * 100)
        b_cm = int(d_back * 100)
        l_cm = int(d_left * 100)
        r_cm = int(d_right * 100)

        oled_dict = {
            'ip': '192.168.1.105',
            'battery_percent': 98,
            'mode': 'DRIVING' if (abs(self.linear_x) > 0.01 or abs(self.angular_z) > 0.01) else 'IDLE',
            'front_cm': f_cm,
            'back_cm': b_cm,
            'left_cm': l_cm,
            'right_cm': r_cm
        }
        s = String()
        s.data = json.dumps(oled_dict)
        self.oled_pub.publish(s)

        if self.oled:
            self.oled.setColor(0x000000)
            self.oled.fillRectangle(0, 0, 128, 64)
            self.oled.setColor(0x00E5FF)
            self.oled.drawText("NodeMCU 4WD Robot", 5, 2)
            self.oled.setColor(0xFFFFFF)
            self.oled.drawText(f"F:{f_cm:3d}cm  B:{b_cm:3d}cm", 5, 18)
            self.oled.drawText(f"L:{l_cm:3d}cm  R:{r_cm:3d}cm", 5, 32)
            self.oled.setColor(0x00FF00 if oled_dict['mode'] == 'IDLE' else 0xFFFF00)
            self.oled.drawText(f"MOD:{oled_dict['mode']} B:%98", 5, 48)

def main():
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())
    if timestep <= 0:
        timestep = 32

    rclpy.init()
    node = WebotsRobotROS2(robot, timestep)

    try:
        while robot.step(timestep) != -1 and rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.001)
            node.update_motors()
            node.publish_sensors()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
