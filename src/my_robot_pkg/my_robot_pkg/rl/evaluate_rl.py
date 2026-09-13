#!/usr/bin/env python3
"""
evaluate_rl.py
--------------
Eğitilmiş Pekiştirmeli Öğrenme modelini (best_model.zip) yükler ve
robotun engellerden kaçarak hedeflere otonom gidişini test eder.
"""

import os
import time
from stable_baselines3 import PPO
from my_robot_pkg.rl.robot_env import RobotEnv

def main():
    model_path = os.path.expanduser("/home/onur/autonomous_robot/src/my_robot_pkg/models/best_model.zip")
    if not os.path.exists(model_path):
        # Eğer best_model yoksa son kaydedilen modeli ara
        models_dir = os.path.expanduser("/home/onur/autonomous_robot/src/my_robot_pkg/models")
        files = [f for f in os.listdir(models_dir) if f.endswith('.zip')] if os.path.exists(models_dir) else []
        if files:
            model_path = os.path.join(models_dir, sorted(files)[-1])
        else:
            print(f"❌ Henüz eğitilmiş model bulunamadı! Lütfen önce 'robot_train' çalıştırın.")
            return

    print("=" * 60)
    print(f"🤖 EĞİTİLMİŞ MODEL TEST EDİLİYOR: {model_path}")
    print("=" * 60)

    env = RobotEnv()
    model = PPO.load(model_path, env=env)

    num_episodes = 20
    success_count = 0

    try:
        for ep in range(1, num_episodes + 1):
            obs, _ = env.reset()
            done = False
            total_reward = 0.0
            print(f"\n[Test Bölümü #{ep:02d}] Yeni Hedef Belirlendi: ({env.goal_x:.2f}, {env.goal_y:.2f})")

            while not done:
                # Deterministic=True: Eğitimdeki rastgele keşif yerine en iyi bildiği aksiyonu seçer
                action, _ = model.predict(obs, deterministic=True)
                obs, reward, terminated, truncated, info = env.step(action)
                total_reward += reward
                done = terminated or truncated

            if info.get("dist_to_goal", 1.0) < 0.22:
                success_count += 1
                print(f"  -> 🏆 BAŞARILI! Hedefe ulaştı. (Toplam Ödül: {total_reward:.2f})")
            else:
                print(f"  -> 💥 Engelle temas veya süre doldu. (Kalan Mesafe: {info.get('dist_to_goal', 0):.2f}m)")

        print("\n" + "=" * 60)
        print(f"📊 TEST SONUCU: {success_count}/{num_episodes} Başarı Oranı: %{success_count/num_episodes * 100:.1f}")
        print("=" * 60)

    except KeyboardInterrupt:
        print("\nTest durduruldu.")
    finally:
        env.close()

if __name__ == '__main__':
    main()
