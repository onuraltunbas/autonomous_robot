"""
Unreal Engine 5 - Live Physics & Teleop Bridge
Runs inside Unreal Editor using unreal.register_slate_post_tick_callback.
- Moves the 3D 'AutonomousBoxRobot' actor in real-time based on ROS 2 /cmd_vel.
- Uses sweep=True for realistic collision with apartment walls and furniture.
- Performs 4 real LineTraces corresponding to the 4 HC-SR04 ultrasonic sensors.
- Streams real odometry and sonar distances back to ROS 2 bridge.
"""

import math
import socket
import struct
import json
import time

try:
    import unreal
    IN_UE = True
except ImportError:
    IN_UE = False

BRIDGE_HOST = '127.0.0.1'
BRIDGE_PORT = 9876

class UnrealLiveRobotBridge:
    _instance = None

    def __init__(self):
        self.sock = None
        self.connected = False
        self.handle = None
        self.robot_actor = None
        
        # Velocity targets from ROS
        self.vx = 0.0
        self.wz = 0.0
        self.target_vx = 0.0
        self.target_wz = 0.0

        # Sonars (meters)
        self.sonars = {'front': 4.0, 'left': 4.0, 'back': 4.0, 'right': 4.0}
        self.last_send_time = 0.0
        self.last_connect_try = 0.0

    @classmethod
    def get(cls):
        if cls._instance is None:
            cls._instance = UnrealLiveRobotBridge()
        return cls._instance

    def start(self):
        if not IN_UE:
            print("[LiveBridge] Error: Must be run inside Unreal Engine Python console.")
            return

        if self.handle is not None:
            try:
                unreal.unregister_slate_post_tick_callback(self.handle)
            except Exception:
                pass

        self.handle = unreal.register_slate_post_tick_callback(self.tick)
        print("=========================================================")
        print("[LiveBridge] OTONOM ROBOT CANLI SÜRÜŞ KÖPRÜSÜ AKTİF!")
        print("[LiveBridge] 3D Robot teleop hareketlerine bağlandı.")
        print("[LiveBridge] 4x HC-SR04 ultrasonik lazer taraması devrede.")
        print("=========================================================")

    def stop(self):
        if self.handle:
            unreal.unregister_slate_post_tick_callback(self.handle)
            self.handle = None
        if self.sock:
            try:
                self.sock.close()
            except Exception:
                pass
            self.sock = None
            self.connected = False
        print("[LiveBridge] Köprü durduruldu.")

    def try_connect(self):
        now = time.time()
        if now - self.last_connect_try < 1.0:
            return
        self.last_connect_try = now

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(0.01)
            self.sock.connect((BRIDGE_HOST, BRIDGE_PORT))
            self.sock.setblocking(False)
            self.connected = True
            print(f"[LiveBridge] ROS 2 Köprüsüne bağlandı ({BRIDGE_HOST}:{BRIDGE_PORT})!")
        except Exception:
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
                    self.target_vx = float(data['cmd_vel']['vx'])
                    self.target_wz = float(data['cmd_vel']['wz'])
        except BlockingIOError:
            pass
        except Exception:
            self.connected = False
            self.sock = None

    def find_robot(self):
        if self.robot_actor and self.robot_actor.is_valid():
            return self.robot_actor

        subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
        for a in subsystem.get_all_level_actors():
            if a.get_actor_label() == 'AutonomousBoxRobot':
                self.robot_actor = a
                return a
        return None

    def perform_sonar_traces(self, robot):
        """Performs 4 real line traces (0, 90, 180, 270 deg) to detect real apartment walls"""
        origin = robot.get_actor_location()
        # Raise trace start slightly above floor (Z + 5 cm)
        start = unreal.Vector(origin.x, origin.y, origin.z + 5.0)

        rot = robot.get_actor_rotation()
        yaw_rad = math.radians(rot.yaw)

        # 4 Directions: Front (yaw), Left (yaw+90), Back (yaw+180), Right (yaw-90)
        angles = {
            'front': yaw_rad,
            'left': yaw_rad + (math.pi / 2.0),
            'back': yaw_rad + math.pi,
            'right': yaw_rad - (math.pi / 2.0)
        }

        max_trace_dist = 400.0  # 4 meters in cm
        world = robot.get_world()

        for key, ang in angles.items():
            dir_vec = unreal.Vector(math.cos(ang), math.sin(ang), 0.0)
            end = unreal.Vector(start.x + dir_vec.x * max_trace_dist,
                                start.y + dir_vec.y * max_trace_dist,
                                start.z)

            # Perform line trace
            hit = unreal.SystemLibrary.line_trace_single(
                world,
                start,
                end,
                unreal.TraceTypeQuery.TRACE_TYPE_QUERY1,
                False,
                [robot],
                unreal.DrawDebugTrace.NONE,
                True,
                unreal.LinearColor(1,0,0,1),
                unreal.LinearColor(0,1,0,1),
                0.0
            )

            if hit:
                # hit.distance is in cm, convert to meters
                dist_m = hit.distance / 100.0
                self.sonars[key] = max(0.02, min(4.0, dist_m))
            else:
                self.sonars[key] = 4.00

    def tick(self, delta_time):
        if not self.connected:
            self.try_connect()

        self.poll_cmd_vel()

        robot = self.find_robot()
        if not robot:
            return

        dt = min(delta_time, 0.1)

        # Smooth acceleration / deceleration
        self.vx += (self.target_vx - self.vx) * min(1.0, 10.0 * dt)
        self.wz += (self.target_wz - self.wz) * min(1.0, 10.0 * dt)

        # Move 3D robot physically in Unreal Engine with collision sweep!
        if abs(self.vx) > 0.001 or abs(self.wz) > 0.001:
            # Yaw rotation in Unreal (degrees)
            # ROS positive angular.z is counter-clockwise (left turn)
            yaw_deg = math.degrees(self.wz * dt)
            robot.add_actor_local_rotation(unreal.Rotator(0.0, yaw_deg, 0.0), sweep=True)

            # Forward translation in Unreal (X cm)
            delta_x_cm = self.vx * dt * 100.0
            robot.add_actor_local_offset(unreal.Vector(delta_x_cm, 0.0, 0.0), sweep=True)

        # Perform 4 real HC-SR04 sonar traces every 50ms
        now = time.time()
        if now - self.last_send_time >= 0.05:
            self.last_send_time = now
            self.perform_sonar_traces(robot)

            # Send telemetry back to ROS 2
            if self.connected and self.sock:
                loc = robot.get_actor_location()
                rot = robot.get_actor_rotation()

                telemetry = {
                    'odom': {
                        'x': loc.x / 100.0,
                        'y': loc.y / 100.0,
                        'yaw': math.radians(rot.yaw),
                        'vx': self.vx,
                        'wz': self.wz
                    },
                    'sonars': self.sonars,
                    'oled': {
                        'ip': '192.168.1.105',
                        'battery_percent': 98,
                        'mode': 'DRIVING' if (abs(self.vx) > 0.01 or abs(self.wz) > 0.01) else 'IDLE',
                        'front_cm': int(self.sonars['front'] * 100),
                        'back_cm': int(self.sonars['back'] * 100),
                        'left_cm': int(self.sonars['left'] * 100),
                        'right_cm': int(self.sonars['right'] * 100)
                    }
                }

                try:
                    payload = json.dumps(telemetry).encode('utf-8')
                    msg = struct.pack('>I', len(payload)) + payload
                    self.sock.sendall(msg)
                except Exception:
                    self.connected = False
                    self.sock = None

def start():
    UnrealLiveRobotBridge.get().start()

def stop():
    UnrealLiveRobotBridge.get().stop()

if __name__ == '__main__':
    start()
