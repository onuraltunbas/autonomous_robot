#!/usr/bin/env python3
"""
Custom Keyboard Teleoperation Node for Autonomous 4WD Robot
Controls:
  [W] : İleri (+X)
  [S] : Geri (-X)
  [A] : Sola Dön (+Yaw)
  [D] : Sağa Dön (-Yaw)
  [X] : Fren / Durdur (Stop)
  [Q] : Doğrusal Hızı Artır
  [Z] : Doğrusal Hızı Azalt
  [Ctrl+C] : Çıkış
"""

import sys
import select
import termios
import tty
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range
from std_msgs.msg import String
import json

INSTRUCTIONS = """
╔══════════════════════════════════════════════════════════╗
║        4WD OTONOM ROBOT - ÖZEL TELEOP KONTROL PANELİ     ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║                     [ W ] : İleri                        ║
║     [ A ] : Sola Dön               [ D ] : Sağa Dön      ║
║                     [ S ] : Geri                         ║
║                                                          ║
║                     [ X ] : FREN (DUR)                   ║
║                                                          ║
║   [ Q ] : Hız Artır (+0.05)   [ Z ] : Hız Azalt (-0.05)  ║
║   [ CTRL + C ] : Çıkış                                   ║
╚══════════════════════════════════════════════════════════╝
"""

class CustomTeleopNode(Node):
    def __init__(self):
        super().__init__('teleop_robot')

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # Telemetry subscribers
        self.sonars = {'front': 0.0, 'left': 0.0, 'back': 0.0, 'right': 0.0}
        self.oled_info = "Bekleniyor..."

        self.create_subscription(Range, '/sensors/sonar_front', lambda m: self.update_sonar('front', m.range), 10)
        self.create_subscription(Range, '/sensors/sonar_left',  lambda m: self.update_sonar('left', m.range), 10)
        self.create_subscription(Range, '/sensors/sonar_back',  lambda m: self.update_sonar('back', m.range), 10)
        self.create_subscription(Range, '/sensors/sonar_right', lambda m: self.update_sonar('right', m.range), 10)
        self.create_subscription(String, '/nodemcu/oled_status', self.oled_callback, 10)

        # Velocity settings
        self.speed_step = 0.05
        self.turn_step = 0.20
        self.max_linear = 0.80   # m/s (~3 km/h for compact robot)
        self.max_angular = 2.50  # rad/s

        self.linear_x = 0.0
        self.angular_z = 0.0

        # UI display timer
        self.create_timer(0.1, self.render_ui)
        # Publishing timer (20 Hz)
        self.create_timer(0.05, self.publish_velocity)

    def update_sonar(self, key, value):
        self.sonars[key] = value

    def oled_callback(self, msg):
        try:
            d = json.loads(msg.data)
            self.oled_info = f"IP: {d.get('ip','-')} | Pil: %{d.get('battery_percent','-')} | Mod: {d.get('mode','-')}"
        except Exception:
            self.oled_info = msg.data

    def publish_velocity(self):
        twist = Twist()
        twist.linear.x = float(self.linear_x)
        twist.angular.z = float(self.angular_z)
        self.cmd_pub.publish(twist)

    def brake(self):
        self.linear_x = 0.0
        self.angular_z = 0.0

    def render_ui(self):
        # Format sonar warnings
        def fmt_sonar(val):
            cm = int(val * 100)
            if cm < 15:
                return f"\033[91m{cm:3d} cm [UYARI!]\033[0m"
            elif cm < 40:
                return f"\033[93m{cm:3d} cm\033[0m"
            else:
                return f"\033[92m{cm:3d} cm\033[0m"

        f_str = fmt_sonar(self.sonars['front'])
        b_str = fmt_sonar(self.sonars['back'])
        l_str = fmt_sonar(self.sonars['left'])
        r_str = fmt_sonar(self.sonars['right'])

        sys.stdout.write(
            f"\r[DURUM] Hız: {self.linear_x:+.2f} m/s | Dönüş: {self.angular_z:+.2f} rad/s | "
            f"Sensörler: [Ön: {f_str} | Sol: {l_str} | Sağ: {r_str} | Arka: {b_str}]  "
        )
        sys.stdout.flush()

def get_key(settings):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.05)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main(args=None):
    settings = termios.tcgetattr(sys.stdin)
    rclpy.init(args=args)
    node = CustomTeleopNode()

    print(INSTRUCTIONS)

    try:
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.01)
            key = get_key(settings)

            if not key:
                continue

            k = key.lower()
            if k == 'w':
                node.linear_x = min(node.max_linear, node.linear_x + node.speed_step)
            elif k == 's':
                node.linear_x = max(-node.max_linear, node.linear_x - node.speed_step)
            elif k == 'a':
                node.angular_z = min(node.max_angular, node.angular_z + node.turn_step)
            elif k == 'd':
                node.angular_z = max(-node.max_angular, node.angular_z - node.turn_step)
            elif k == 'x':
                node.brake()
            elif k == 'q':
                node.speed_step = min(0.20, node.speed_step + 0.02)
                node.turn_step  = min(0.50, node.turn_step + 0.05)
            elif k == 'z':
                node.speed_step = max(0.01, node.speed_step - 0.02)
                node.turn_step  = max(0.05, node.turn_step - 0.05)
            elif key == '\x03':  # Ctrl+C
                break

    except Exception as e:
        print(f"\n[HATA] Teleop: {e}")
    finally:
        node.brake()
        node.publish_velocity()
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()
        print("\n[BİLGİ] Teleop kapatıldı. Robot frenlendi.")

if __name__ == '__main__':
    main()
