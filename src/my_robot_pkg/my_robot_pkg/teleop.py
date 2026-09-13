#!/usr/bin/env python3
import sys
import termios
import tty
import select
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

BANNER = """
===================================================
         ROBOT TELEOP KLAVYE KONTROLÜ
===================================================
Hareket Tuşları:
   [w] : İleri
   [s] : Geri
   [a] : Sola Dön
   [d] : Sağa Dön
   [x] : Dur (veya Space)

Hız Ayarı:
   [e] : Hızı Artır (+%10)
   [q] : Hızı Azalt (-%10)

Çıkış:
   Ctrl+C
===================================================
"""

class TeleopNode(Node):
    def __init__(self):
        super().__init__('teleop_node')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        # Varsayılan hızlar
        self.linear_speed = 0.3   # m/s
        self.angular_speed = 1.0  # rad/s

        self.speed_step = 0.05
        self.turn_step = 0.1

    def update_speed(self, multiplier):
        self.linear_speed = max(0.05, min(2.0, self.linear_speed * multiplier))
        self.angular_speed = max(0.1, min(5.0, self.angular_speed * multiplier))
        self.print_status("Hız Güncellendi")

    def publish_twist(self, linear, angular, action=""):
        twist = Twist()
        twist.linear.x = float(linear)
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = float(angular)
        self.publisher_.publish(twist)
        if action:
            self.print_status(action)

    def print_status(self, action=""):
        status_msg = f"\r[Durum: {action:<14}] Çizgisel Hız: {self.linear_speed:.2f} m/s | Açısal Hız: {self.angular_speed:.2f} rad/s    "
        sys.stdout.write(status_msg)
        sys.stdout.flush()

def get_key(settings):
    tty.setraw(sys.stdin.fileno())
    # 0.1 saniye bekle
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main(args=None):
    # Terminal ayarlarını yedekle
    settings = termios.tcgetattr(sys.stdin)

    rclpy.init(args=args)
    node = TeleopNode()

    print(BANNER)
    node.print_status("Hazır")

    try:
        while rclpy.ok():
            key = get_key(settings)

            if key == 'w':
                node.publish_twist(node.linear_speed, 0.0, "İLERİ")
            elif key == 's':
                node.publish_twist(-node.linear_speed, 0.0, "GERİ")
            elif key == 'a':
                node.publish_twist(0.0, node.angular_speed, "SOLA DÖN")
            elif key == 'd':
                node.publish_twist(0.0, -node.angular_speed, "SAĞA DÖN")
            elif key == 'x' or key == ' ':
                node.publish_twist(0.0, 0.0, "DURDU")
            elif key == 'e':
                # Hızı %10 artır
                node.update_speed(1.1)
            elif key == 'q':
                # Hızı %10 azalt
                node.update_speed(0.9)
            elif key == '\x03':  # Ctrl+C
                break

            rclpy.spin_once(node, timeout_sec=0)

    except Exception as e:
        print(f"\nHata: {e}")
    finally:
        # Robotu güvenli bir şekilde durdur
        node.publish_twist(0.0, 0.0, "KAPATILDI")
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()
        print("\nTeleop sonlandırıldı.\n")

if __name__ == '__main__':
    main()
