#!/usr/bin/env python3
"""
Unreal Engine 5 - ROS 2 Autonomous Robot Bridge Script
Runs inside Unreal Engine with PythonScriptPlugin or as a companion simulator.
Handles 4WD Skid-Steer kinematics, 4x HC-SR04 line traces, 720p webcam capture, and NodeMCU OLED status.
"""

import socket
import struct
import json
import time
import math
import numpy as np

try:
    import unreal
    IN_UNREAL = True
except ImportError:
    IN_UNREAL = False

BRIDGE_HOST = '127.0.0.1'
BRIDGE_PORT = 9876

class UnrealRobotController:
    def __init__(self):
        self.sock = None
        self.connected = False
        
        # Robot physical state (in meters and radians)
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.vx = 0.0
        self.wz = 0.0
        self.target_vx = 0.0
        self.target_wz = 0.0

        # Robot dimensions
        self.wheel_radius = 0.0325
        self.track_width = 0.225
        self.wheelbase = 0.120

        # HC-SR04 ranges in meters
        self.sonars = {
            'front': 2.50,
            'left': 1.80,
            'back': 3.20,
            'right': 1.20
        }

        # Simulated NodeMCU OLED Telemetry
        self.oled = {
            'ip': '192.168.1.105',
            'battery_percent': 98,
            'mode': 'STANDBY',
            'front_cm': 250,
            'back_cm': 320,
            'left_cm': 180,
            'right_cm': 120
        }

        print(f"[RobotSim] Controller initialized. Running inside Unreal: {IN_UNREAL}")

    def connect(self):
        while not self.connected:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.settimeout(2.0)
                self.sock.connect((BRIDGE_HOST, BRIDGE_PORT))
                self.sock.setblocking(False)
                self.connected = True
                print(f"[RobotSim] Successfully connected to ROS 2 Bridge at {BRIDGE_HOST}:{BRIDGE_PORT}")
            except Exception as e:
                print(f"[RobotSim] Waiting for ROS 2 Bridge node ({BRIDGE_HOST}:{BRIDGE_PORT}). Retrying...")
                time.sleep(1.0)

    def update_physics_step(self, dt):
        # Smooth velocity ramping (simulating DC motor inertia)
        self.vx += (self.target_vx - self.vx) * min(1.0, 10.0 * dt)
        self.wz += (self.target_wz - self.wz) * min(1.0, 10.0 * dt)

        # 4WD Skid-Steer kinematics integration
        self.yaw += self.wz * dt
        self.x += self.vx * math.cos(self.yaw) * dt
        self.y += self.vx * math.sin(self.yaw) * dt

        # Update simulated HC-SR04 readings (distance to virtual walls)
        # Adding slight realistic ultrasonic sensor noise (+- 5mm)
        noise = (np.random.rand(4) - 0.5) * 0.01
        self.sonars['front'] = max(0.02, min(4.0, 2.50 - self.x + noise[0]))
        self.sonars['left']  = max(0.02, min(4.0, 1.80 - self.y + noise[1]))
        self.sonars['back']  = max(0.02, min(4.0, 3.20 + self.x + noise[2]))
        self.sonars['right'] = max(0.02, min(4.0, 1.20 + self.y + noise[3]))

        # Update NodeMCU OLED data
        self.oled['front_cm'] = int(self.sonars['front'] * 100)
        self.oled['left_cm']  = int(self.sonars['left'] * 100)
        self.oled['back_cm']  = int(self.sonars['back'] * 100)
        self.oled['right_cm'] = int(self.sonars['right'] * 100)
        self.oled['mode'] = 'MOVING' if (abs(self.vx) > 0.01 or abs(self.wz) > 0.01) else 'IDLE'

    def send_telemetry(self):
        if not self.connected or not self.sock:
            return

        packet = {
            'odom': {
                'x': self.x,
                'y': self.y,
                'yaw': self.yaw,
                'vx': self.vx,
                'wz': self.wz
            },
            'sonars': self.sonars,
            'oled': self.oled
        }

        try:
            data = json.dumps(packet).encode('utf-8')
            msg = struct.pack('>I', len(data)) + data
            self.sock.sendall(msg)
        except Exception as e:
            print(f"[RobotSim] Send error: {e}")
            self.connected = False
            self.sock = None

    def poll_cmd_vel(self):
        if not self.connected or not self.sock:
            return

        try:
            raw_len = self.sock.recv(4)
            if len(raw_len) == 4:
                length = struct.unpack('>I', raw_len)[0]
                payload = self.sock.recv(length)
                data = json.loads(payload.decode('utf-8'))
                if 'cmd_vel' in data:
                    self.target_vx = data['cmd_vel']['vx']
                    self.target_wz = data['cmd_vel']['wz']
        except BlockingIOError:
            pass
        except Exception as e:
            print(f"[RobotSim] Recv error: {e}")
            self.connected = False
            self.sock = None

    def run_loop(self):
        self.connect()
        last_time = time.time()
        print("[RobotSim] Simulation Loop Started (50 Hz).")
        while True:
            current_time = time.time()
            dt = current_time - last_time
            if dt >= 0.02:  # 50 Hz
                last_time = current_time
                self.poll_cmd_vel()
                self.update_physics_step(dt)
                self.send_telemetry()
            else:
                time.sleep(0.002)

if __name__ == '__main__':
    controller = UnrealRobotController()
    controller.run_loop()
