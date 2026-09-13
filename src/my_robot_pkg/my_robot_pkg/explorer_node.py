#!/usr/bin/env python3
"""
explorer_node.py
----------------
Robot süpürge mantığıyla odayı otonom olarak gezer (duvar takip etme ve serbest alan keşfi).
4 ultrasonik sensör verisini kullanarak engellere çarpmadan tüm haritayı tarar.
/explore/start konusu üzerinden (veya doğrudan) başlatılıp durdurulabilir.
"""

import time
import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class ExplorerNode(Node):
    def __init__(self):
        super().__init__('explorer_node')

        # Sensör mesafeleri (başlangıçta sonsuz)
        self.front_dist = 4.0
        self.left_dist = 4.0
        self.back_dist = 4.0
        self.right_dist = 4.0

        # Keşif Durumu
        self.is_exploring = True  # Başlangıçta aktif (veya tetiklenebilir)
        self.state = 'FORWARD'    # FORWARD, TURN_LEFT, TURN_RIGHT, BACKUP
        self.state_timer = 0.0

        # Hız Parametreleri
        self.linear_speed = 0.20   # 20 cm/s
        self.turn_speed = 0.70     # 0.7 rad/s

        # Güvenlik Eşikleri (metre)
        self.safe_front_distance = 0.40
        self.emergency_distance = 0.22
        self.side_wall_distance = 0.35

        # Abonelikler
        self.create_subscription(Range, '/sonar/front', self.front_cb, 10)
        self.create_subscription(Range, '/sonar/left', self.left_cb, 10)
        self.create_subscription(Range, '/sonar/back', self.back_cb, 10)
        self.create_subscription(Range, '/sonar/right', self.right_cb, 10)

        # Keşfi dışarıdan başlatma/durdurma konusu
        self.create_subscription(Bool, '/explore/start', self.control_cb, 10)

        # Motor komut yayıncısı
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # Kontrol Döngüsü: 10 Hz (Her 100ms'de bir karar ver)
        self.timer = self.create_timer(0.1, self.control_loop)
        self.get_logger().info('Otonom Keşif (Süpürge Modu) Düğümü Başlatıldı. Durum: AKTİF')

    def front_cb(self, msg: Range):
        self.front_dist = msg.range if 0.02 <= msg.range <= 4.0 else 4.0

    def left_cb(self, msg: Range):
        self.left_dist = msg.range if 0.02 <= msg.range <= 4.0 else 4.0

    def back_cb(self, msg: Range):
        self.back_dist = msg.range if 0.02 <= msg.range <= 4.0 else 4.0

    def right_cb(self, msg: Range):
        self.right_dist = msg.range if 0.02 <= msg.range <= 4.0 else 4.0

    def control_cb(self, msg: Bool):
        self.is_exploring = msg.data
        if not self.is_exploring:
            self.stop_robot()
            self.get_logger().info('Otonom Keşif Durduruldu.')
        else:
            self.get_logger().info('Otonom Keşif Başlatıldı.')

    def stop_robot(self):
        twist = Twist()
        self.cmd_pub.publish(twist)

    def control_loop(self):
        if not self.is_exploring:
            return

        twist = Twist()
        current_time = time.time()

        if self.state == 'BACKUP':
            if current_time < self.state_timer and self.back_dist > 0.20:
                twist.linear.x = -self.linear_speed
                twist.angular.z = self.turn_speed if self.left_dist > self.right_dist else -self.turn_speed
            else:
                self.state = 'TURN_LEFT' if self.left_dist > self.right_dist else 'TURN_RIGHT'
                self.state_timer = current_time + 1.5

        elif self.state in ['TURN_LEFT', 'TURN_RIGHT']:
            if current_time < self.state_timer and self.front_dist < self.safe_front_distance:
                twist.linear.x = 0.0
                twist.angular.z = self.turn_speed if self.state == 'TURN_LEFT' else -self.turn_speed
            else:
                self.state = 'FORWARD'

        elif self.state == 'FORWARD':
            if self.front_dist < self.emergency_distance:
                self.state = 'BACKUP'
                self.state_timer = current_time + 1.2
            elif self.front_dist < self.safe_front_distance:
                self.state = 'TURN_LEFT' if self.left_dist > self.right_dist else 'TURN_RIGHT'
                self.state_timer = current_time + 1.2
            else:
                twist.linear.x = self.linear_speed
                if self.left_dist < 0.25:
                    twist.angular.z = -0.3
                elif self.right_dist < 0.25:
                    twist.angular.z = 0.3
                else:
                    twist.angular.z = 0.0

        self.cmd_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ExplorerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.stop_robot()
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
