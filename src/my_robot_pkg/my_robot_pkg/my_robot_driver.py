import math
import rclpy
from geometry_msgs.msg import Twist, TransformStamped
from nav_msgs.msg import Odometry
import tf2_ros

class MyRobotDriver:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot
        self.__time_step = int(self.__robot.getBasicTimeStep())

        # Webots motorlarını alıyoruz
        self.__left_motor = self.__robot.getDevice('left_wheel_motor')
        self.__right_motor = self.__robot.getDevice('right_wheel_motor')

        # Motorları sonsuz dönüş (hız kontrolü) moduna alıyoruz
        self.__left_motor.setPosition(float('inf'))
        self.__left_motor.setVelocity(0.0)
        self.__right_motor.setPosition(float('inf'))
        self.__right_motor.setVelocity(0.0)

        # Tekerlek enkoderlerini (PositionSensor) alıyoruz
        self.__left_sensor = self.__robot.getDevice('left_wheel_sensor')
        self.__right_sensor = self.__robot.getDevice('right_wheel_sensor')
        if self.__left_sensor:
            self.__left_sensor.enable(self.__time_step)
        if self.__right_sensor:
            self.__right_sensor.enable(self.__time_step)

        self.__wheel_radius = 0.04       # 4 cm
        self.__wheel_separation = 0.22   # İki tekerlek arası mesafe: 2 * 0.11m = 0.22m

        # Odometri değişkenleri (x, y, yaw)
        self.__x = 0.0
        self.__y = 0.0
        self.__yaw = 0.0
        self.__prev_left_pos = 0.0
        self.__prev_right_pos = 0.0
        self.__first_step = True

        self.__target_twist = Twist()

        # ROS 2 Node'unu başlatıyoruz
        rclpy.init(args=None)
        self.__node = rclpy.create_node('my_robot_driver')
        self.__node.create_subscription(Twist, 'cmd_vel', self.__cmd_vel_callback, 1)

        # Odometri Publisher ve TF Broadcaster
        self.__odom_pub = self.__node.create_publisher(Odometry, 'odom', 10)
        self.__tf_broadcaster = tf2_ros.TransformBroadcaster(self.__node)

    def __cmd_vel_callback(self, twist):
        self.__target_twist = twist

    def step(self):
        # ROS 2'den gelen yön komutlarını okuyoruz
        rclpy.spin_once(self.__node, timeout_sec=0)

        forward_speed = self.__target_twist.linear.x
        angular_speed = self.__target_twist.angular.z

        # Diferansiyel Sürüş Matematiği (Tekerlek yarıçapı: 0.04m, Merkezden uzaklık: 0.11m)
        command_motor_left = (forward_speed - angular_speed * 0.11) / self.__wheel_radius
        command_motor_right = (forward_speed + angular_speed * 0.11) / self.__wheel_radius

        # Hız komutlarını Webots motorlarına gönderiyoruz
        self.__left_motor.setVelocity(command_motor_left)
        self.__right_motor.setVelocity(command_motor_right)

        # Odometri Hesaplama (Enkoderlerden)
        if self.__left_sensor and self.__right_sensor:
            curr_left = self.__left_sensor.getValue()
            curr_right = self.__right_sensor.getValue()

            if self.__first_step:
                self.__prev_left_pos = curr_left
                self.__prev_right_pos = curr_right
                self.__first_step = False
                return

            d_left = (curr_left - self.__prev_left_pos) * self.__wheel_radius
            d_right = (curr_right - self.__prev_right_pos) * self.__wheel_radius
            self.__prev_left_pos = curr_left
            self.__prev_right_pos = curr_right

            d_center = (d_right + d_left) / 2.0
            d_yaw = (d_right - d_left) / self.__wheel_separation

            # Konum güncelleme
            self.__yaw += d_yaw
            self.__yaw = math.atan2(math.sin(self.__yaw), math.cos(self.__yaw))  # [-pi, pi] normalize
            self.__x += d_center * math.cos(self.__yaw)
            self.__y += d_center * math.sin(self.__yaw)

            current_time = self.__node.get_clock().now().to_msg()

            # Quaternion dönüşümü (Yaw -> Quaternion)
            qz = math.sin(self.__yaw / 2.0)
            qw = math.cos(self.__yaw / 2.0)

            # 1. TF Dönüşümü Yayınlama (odom -> base_link)
            t = TransformStamped()
            t.header.stamp = current_time
            t.header.frame_id = 'odom'
            t.child_frame_id = 'base_link'
            t.transform.translation.x = self.__x
            t.transform.translation.y = self.__y
            t.transform.translation.z = 0.0
            t.transform.rotation.x = 0.0
            t.transform.rotation.y = 0.0
            t.transform.rotation.z = qz
            t.transform.rotation.w = qw
            self.__tf_broadcaster.sendTransform(t)

            # 2. Odometri Mesajı Yayınlama (/odom)
            odom = Odometry()
            odom.header.stamp = current_time
            odom.header.frame_id = 'odom'
            odom.child_frame_id = 'base_link'
            odom.pose.pose.position.x = self.__x
            odom.pose.pose.position.y = self.__y
            odom.pose.pose.position.z = 0.0
            odom.pose.pose.orientation.x = 0.0
            odom.pose.pose.orientation.y = 0.0
            odom.pose.pose.orientation.z = qz
            odom.pose.pose.orientation.w = qw
            odom.twist.twist.linear.x = forward_speed
            odom.twist.twist.angular.z = angular_speed
            self.__odom_pub.publish(odom)
