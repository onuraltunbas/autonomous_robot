"""
robot_env.py
------------
Webots simülasyonunu ve ROS 2 düğümlerini Gymnasium (OpenAI Gym) uyumlu
bir Pekiştirmeli Öğrenme (RL) ortamına dönüştüren çevre sınıfı.
"""

import math
import random
import time
import numpy as np
import gymnasium as gym
from gymnasium import spaces

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, PoseStamped

class RobotEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self):
        super().__init__()

        # ==========================================================
        # 1. GÖZLEM UZAYI (OBSERVATION SPACE) - Robotun Hissettikleri
        # ==========================================================
        # 6 Boyutlu Vektör:
        # [0]: Ön Sonar Mesafesi (0.0 - 4.0 m arası, normalize: 0.0 - 1.0)
        # [1]: Sol Sonar Mesafesi (0.0 - 4.0 m arası, normalize: 0.0 - 1.0)
        # [2]: Arka Sonar Mesafesi (0.0 - 4.0 m arası, normalize: 0.0 - 1.0)
        # [3]: Sağ Sonar Mesafesi (0.0 - 4.0 m arası, normalize: 0.0 - 1.0)
        # [4]: Hedefe Kalan Mesafe (metre cinsinden, örn: 0.0 - 8.0 m)
        # [5]: Hedefe Olan Açı Farkı (-pi ile +pi radyan arası)
        
        self.observation_space = spaces.Box(
            low=np.array([0.0, 0.0, 0.0, 0.0, 0.0, -np.pi], dtype=np.float32),
            high=np.array([1.0, 1.0, 1.0, 1.0, 8.0, np.pi], dtype=np.float32),
            dtype=np.float32
        )

        # ==========================================================
        # 2. AKSİYON UZAYI (ACTION SPACE) - Robotun Kararları
        # ==========================================================
        # 2 Boyutlu Sürekli (Continuous) Vektör:
        # [0]: Çizgisel Hız (Linear Velocity) -> [-0.25, 0.25] m/s (İleri / Geri)
        # [1]: Açısal Hız (Angular Velocity)  -> [-1.20, 1.20] rad/s (Dönüş)
        
        self.action_space = spaces.Box(
            low=np.array([-0.25, -1.20], dtype=np.float32),
            high=np.array([0.25, 1.20], dtype=np.float32),
            dtype=np.float32
        )

        # ==========================================================
        # 3. ÖDÜL VE CEZA AYARLARI (REWARD HYPERPARAMETERS)
        # ==========================================================
        self.REWARD_GOAL_REACHED = 100.0   # Hedefe varınca verilecek büyük ödül
        self.PENALTY_COLLISION   = -60.0   # Duvara/engele çarpma cezası
        self.PENALTY_STEP        = -0.05   # Her adımda verilen küçük zaman cezası (hızlı gitmeyi teşvik eder)
        self.REWARD_APPROACH_MUL = 8.0     # Hedefe her yaklaştığı cm başına verilen ödül çarpanı

        # Güvenlik ve Mesafe Eşikleri
        self.COLLISION_DISTANCE = 0.15     # 15 cm'den az kalırsa ÇARPIŞMA say
        self.GOAL_REACH_DISTANCE = 0.20    # Hedefe 20 cm yaklaşırsa BAŞARILI say

        # Robot ve Hedef Durumları
        self.robot_x = 0.0
        self.robot_y = 0.0
        self.robot_yaw = 0.0

        self.front_dist = 4.0
        self.left_dist = 4.0
        self.back_dist = 4.0
        self.right_dist = 4.0

        self.goal_x = 1.0
        self.goal_y = 1.0
        self.prev_distance_to_goal = 0.0
        self.step_count = 0
        self.max_steps_per_episode = 300   # Bir denemede maksimum 300 adım

        # ROS 2 İletişimi
        if not rclpy.ok():
            rclpy.init(args=None)
        self.node = rclpy.create_node('robot_rl_env')

        # Abonelikler
        self.node.create_subscription(Range, '/sonar/front', self._front_cb, 10)
        self.node.create_subscription(Range, '/sonar/left', self._left_cb, 10)
        self.node.create_subscription(Range, '/sonar/back', self._back_cb, 10)
        self.node.create_subscription(Range, '/sonar/right', self._right_cb, 10)
        self.node.create_subscription(Odometry, '/odom', self._odom_cb, 10)

        # Yayıncılar
        self.cmd_pub = self.node.create_publisher(Twist, '/cmd_vel', 10)
        self.goal_pub = self.node.create_publisher(PoseStamped, '/goal_pose', 10)

    def _front_cb(self, msg: Range):
        self.front_dist = msg.range if 0.02 <= msg.range <= 4.0 else 4.0

    def _left_cb(self, msg: Range):
        self.left_dist = msg.range if 0.02 <= msg.range <= 4.0 else 4.0

    def _back_cb(self, msg: Range):
        self.back_dist = msg.range if 0.02 <= msg.range <= 4.0 else 4.0

    def _right_cb(self, msg: Range):
        self.right_dist = msg.range if 0.02 <= msg.range <= 4.0 else 4.0

    def _odom_cb(self, msg: Odometry):
        self.robot_x = msg.pose.pose.position.x
        self.robot_y = msg.pose.pose.position.y
        qz = msg.pose.pose.orientation.z
        qw = msg.pose.pose.orientation.w
        self.robot_yaw = math.atan2(2.0 * (qw * qz), 1.0 - 2.0 * (qz * qz))

    def _get_obs(self):
        # 1. Hedefe olan mesafe
        dx = self.goal_x - self.robot_x
        dy = self.goal_y - self.robot_y
        dist_to_goal = math.sqrt(dx * dx + dy * dy)

        # 2. Hedefe olan açı farkı (Robotun baktığı yön ile hedefin açısı)
        target_angle = math.atan2(dy, dx)
        angle_diff = target_angle - self.robot_yaw
        # Açı farkını [-pi, pi] aralığına normalize et
        angle_diff = math.atan2(math.sin(angle_diff), math.cos(angle_diff))

        # Sonar mesafelerini [0.0, 1.0] aralığına normalize et
        obs = np.array([
            self.front_dist / 4.0,
            self.left_dist / 4.0,
            self.back_dist / 4.0,
            self.right_dist / 4.0,
            dist_to_goal,
            angle_diff
        ], dtype=np.float32)

        return obs, dist_to_goal, angle_diff

    def _spin_ros(self):
        # ROS 2 mesajlarını işle
        for _ in range(3):
            rclpy.spin_once(self.node, timeout_sec=0.01)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.step_count = 0

        # Robotu durdur
        twist = Twist()
        self.cmd_pub.publish(twist)
        self._spin_ros()

        # Harita içinde rastgele yeni bir hedef seç
        # (Arena 5x5m olduğundan [-1.8, 1.8] güvenli alanda hedef seçiyoruz)
        self.goal_x = random.uniform(-1.6, 1.6)
        self.goal_y = random.uniform(-1.6, 1.6)

        # Hedefi RViz'e yayınla
        goal_msg = PoseStamped()
        goal_msg.header.stamp = self.node.get_clock().now().to_msg()
        goal_msg.header.frame_id = 'odom'
        goal_msg.pose.position.x = self.goal_x
        goal_msg.pose.position.y = self.goal_y
        self.goal_pub.publish(goal_msg)

        self._spin_ros()
        obs, dist_to_goal, _ = self._get_obs()
        self.prev_distance_to_goal = dist_to_goal

        return obs, {}

    def step(self, action):
        self.step_count += 1

        # 1. Yapay zekanın seçtiği aksiyonu motorlara gönder
        v = float(action[0])
        w = float(action[1])

        twist = Twist()
        twist.linear.x = v
        twist.angular.z = w
        self.cmd_pub.publish(twist)

        # Simülasyonun adım atması için kısa bekleme ve ROS güncellemesi (100ms)
        time.sleep(0.08)
        self._spin_ros()

        # 2. Yeni gözlemleri al
        obs, dist_to_goal, angle_diff = self._get_obs()

        # 3. Ödül Hesaplama
        # Yaklaşma Ödülü: Önceki adıma göre hedefe yaklaştıysa pozitif, uzaklaştıysa negatif
        approach_reward = (self.prev_distance_to_goal - dist_to_goal) * self.REWARD_APPROACH_MUL
        self.prev_distance_to_goal = dist_to_goal

        reward = approach_reward + self.PENALTY_STEP

        # Açı hizalama bonusu (hedefe doğru bakıyorsa küçük ekstra ödül)
        if abs(angle_diff) < 0.3:
            reward += 0.1

        terminated = False
        truncated = False

        # 4. Çarpışma Kontrolü (4 Sonardan herhangi biri limite değerse)
        min_sonar = min(self.front_dist, self.left_dist, self.right_dist, self.back_dist)
        if min_sonar < self.COLLISION_DISTANCE:
            # Çarpışma oldu!
            reward += self.PENALTY_COLLISION
            terminated = True
            self.stop()

        # 5. Hedefe Ulaşma Kontrolü
        elif dist_to_goal < self.GOAL_REACH_DISTANCE:
            # Başarıyla hedefe ulaştı!
            reward += self.REWARD_GOAL_REACHED
            terminated = True
            self.stop()

        # 6. Zaman Aşımı Kontrolü
        if self.step_count >= self.max_steps_per_episode:
            truncated = True
            self.stop()

        return obs, reward, terminated, truncated, {
            "dist_to_goal": dist_to_goal,
            "min_sonar": min_sonar
        }

    def stop(self):
        twist = Twist()
        self.cmd_pub.publish(twist)
        self._spin_ros()

    def close(self):
        self.stop()
        self.node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
