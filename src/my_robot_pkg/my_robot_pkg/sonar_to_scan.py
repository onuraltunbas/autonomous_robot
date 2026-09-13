#!/usr/bin/env python3
"""
sonar_to_scan.py
----------------
4 adet HC-SR04 ultrasonik sensörden (Ön, Sol, Arka, Sağ) gelen sensor_msgs/Range
verilerini birleştirerek standart 2D sensor_msgs/LaserScan (/scan) formatına dönüştürür.
Bu sayede SLAM (slam_toolbox) ve Nav2 algoritmaları LiDAR varmış gibi haritalama yapabilir.
"""

import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range, LaserScan

class SonarToScan(Node):
    def __init__(self):
        super().__init__('sonar_to_scan')

        # Sonar ölçümlerini tutacağımız değişkenler (başlangıçta sonsuz mesafe)
        self.front_dist = float('inf')
        self.left_dist = float('inf')
        self.back_dist = float('inf')
        self.right_dist = float('inf')

        # HC-SR04 Sensör Parametreleri
        self.min_range = 0.02   # 2 cm
        self.max_range = 4.00   # 4 metre
        self.cone_angle_deg = 15  # Sonar yayılım konisi (±7.5 derece)

        # 4 Sonar konusuna abone oluyoruz
        self.create_subscription(Range, '/sonar/front', self.front_callback, 10)
        self.create_subscription(Range, '/sonar/left', self.left_callback, 10)
        self.create_subscription(Range, '/sonar/back', self.back_callback, 10)
        self.create_subscription(Range, '/sonar/right', self.right_callback, 10)

        # Birleştirilmiş /scan konusunu yayınlayan publisher
        self.scan_pub = self.create_publisher(LaserScan, '/scan', 10)

        # 20 Hz frekansında /scan yayını yapan timer
        self.timer = self.create_timer(0.05, self.publish_scan)
        self.get_logger().info('Sonar to LaserScan Dönüştürücü Düğüm Başlatıldı.')

    def front_callback(self, msg: Range):
        self.front_dist = msg.range if self.min_range <= msg.range <= self.max_range else float('inf')

    def left_callback(self, msg: Range):
        self.left_dist = msg.range if self.min_range <= msg.range <= self.max_range else float('inf')

    def back_callback(self, msg: Range):
        self.back_dist = msg.range if self.min_range <= msg.range <= self.max_range else float('inf')

    def right_callback(self, msg: Range):
        self.right_dist = msg.range if self.min_range <= msg.range <= self.max_range else float('inf')

    def publish_scan(self):
        scan_msg = LaserScan()
        scan_msg.header.stamp = self.get_clock().now().to_msg()
        scan_msg.header.frame_id = 'base_link'

        # -180 derece (-pi) ile +180 derece (+pi) arası 360 ışınlık tarama
        scan_msg.angle_min = -math.pi
        scan_msg.angle_max = math.pi
        scan_msg.angle_increment = math.radians(1.0)  # Her 1 derecede bir ışın (toplam 360 ışın)
        scan_msg.time_increment = 0.0
        scan_msg.scan_time = 0.05
        scan_msg.range_min = self.min_range
        scan_msg.range_max = self.max_range

        num_readings = int(round((scan_msg.angle_max - scan_msg.angle_min) / scan_msg.angle_increment))
        ranges = [float('inf')] * num_readings

        # Sensör Merkez Açıları (Radyan cinsinden, angle_min = -pi referanslı):
        # Sağ: -90° (-pi/2)
        # Ön:    0° (0)
        # Sol: +90° (+pi/2)
        # Arka: 180° (pi veya -pi)
        
        half_cone = math.radians(self.cone_angle_deg / 2.0)

        def angle_to_index(angle_rad):
            # angle_rad [-pi, pi] aralığını [0, num_readings-1] indeksine dönüştürür
            norm_angle = (angle_rad - scan_msg.angle_min) / (scan_msg.angle_max - scan_msg.angle_min)
            idx = int(norm_angle * num_readings)
            return max(0, min(num_readings - 1, idx))

        def fill_cone(center_angle_rad, distance):
            if math.isinf(distance):
                return
            min_idx = angle_to_index(center_angle_rad - half_cone)
            max_idx = angle_to_index(center_angle_rad + half_cone)
            for i in range(min_idx, max_idx + 1):
                ranges[i] = distance

        # 4 Sonar verisini ilgili yay açısına doldur
        fill_cone(0.0, self.front_dist)                  # Ön (0 derece)
        fill_cone(math.pi / 2.0, self.left_dist)         # Sol (+90 derece)
        fill_cone(-math.pi / 2.0, self.right_dist)       # Sağ (-90 derece)
        
        # Arka sensör (-pi ve +pi sınırında olduğu için iki uca da dolduruyoruz)
        if not math.isinf(self.back_dist):
            # +pi ucu
            fill_cone(math.pi, self.back_dist)
            # -pi ucu
            fill_cone(-math.pi, self.back_dist)

        scan_msg.ranges = ranges
        self.scan_pub.publish(scan_msg)

def main(args=None):
    rclpy.init(args=args)
    node = SonarToScan()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
