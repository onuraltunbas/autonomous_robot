#!/usr/bin/env python3
"""
train_rl.py
-----------
PPO (Proximal Policy Optimization) algoritması ile robotu hedefe gitme
ve engellerden kaçma görevinde eğiten ana Pekiştirmeli Öğrenme betiği.
"""

import os
import sys
from datetime import datetime
import torch

from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import CheckpointCallback, BaseCallback
from my_robot_pkg.rl.robot_env import RobotEnv

class TrainingVisualLogger(BaseCallback):
    """
    Her 10 adımda bir terminale temiz ve anlaşılır ilerleme raporu basar.
    """
    def __init__(self, verbose=0):
        super().__init__(verbose)
        self.episode_count = 0

    def _on_step(self) -> bool:
        # Her bölüm bittiğinde bilgi yazdır
        if self.locals.get("dones") is not None and any(self.locals["dones"]):
            self.episode_count += 1
            infos = self.locals.get("infos", [{}])[0]
            dist = infos.get("dist_to_goal", 0.0)
            sonar = infos.get("min_sonar", 0.0)
            
            status = "🏆 HEDEFE ULAŞTI" if dist < 0.22 else ("💥 ÇARPIŞTI" if sonar < 0.16 else "⏳ SÜRE BİTTİ")
            print(f"[Bölüm #{self.episode_count:03d}] Adım: {self.num_timesteps:06d} | Durum: {status:<16} | Kalan Mesafe: {dist:.2f}m | En Yakın Engel: {sonar:.2f}m")
        return True

def main():
    print("=" * 65)
    print("🤖 ROBOT BEBEK - PEKİŞTİRMELİ ÖĞRENME (RL) EĞİTİMİ BAŞLIYOR")
    print("=" * 65)

    # 1. Çıktı ve Kayıt Dizinleri
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    models_dir = os.path.expanduser(f"/home/onur/autonomous_robot/src/my_robot_pkg/models")
    logs_dir = os.path.expanduser(f"/home/onur/autonomous_robot/src/my_robot_pkg/runs/ppo_{timestamp}")
    os.makedirs(models_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)

    print(f"📁 Model Kayıt Yeri     : {models_dir}")
    print(f"📊 TensorBoard Log Yeri : {logs_dir}\n")

    # 2. Gymnasium Ortamını Başlat
    print("🔌 Webots & ROS 2 Ortamına bağlanılıyor...")
    env = RobotEnv()

    # 3. Mevcut Model Kontrolü (Devam Etme / Sıfırdan Başlama)
    force_scratch = "--scratch" in sys.argv or "--reset" in sys.argv
    latest_model_path = None
    
    if not force_scratch:
        interrupted_path = os.path.join(models_dir, "interrupted_model.zip")
        best_path = os.path.join(models_dir, "best_model.zip")
        
        if os.path.exists(interrupted_path):
            latest_model_path = interrupted_path
        elif os.path.exists(best_path):
            latest_model_path = best_path
        else:
            checkpoints = [f for f in os.listdir(models_dir) if f.startswith("robot_ppo_model_") and f.endswith(".zip")]
            if checkpoints:
                # En yüksek adım sayısına sahip checkpoint'i bul
                checkpoints.sort(key=lambda x: int(x.split("_")[3]) if len(x.split("_")) > 3 and x.split("_")[3].isdigit() else 0)
                latest_model_path = os.path.join(models_dir, checkpoints[-1])

    policy_kwargs = dict(
        net_arch=dict(pi=[128, 128], vf=[128, 128])  # 2 Gizli katman, 128'er nöron
    )

    if latest_model_path and os.path.exists(latest_model_path):
        print(f"🔄 Önceki eğitimden model bulundu! Kaldığı yerden devam ediliyor:")
        print(f"   📂 Yüklenen: {latest_model_path}\n")
        model = PPO.load(
            latest_model_path,
            env=env,
            learning_rate=3e-4,
            n_steps=1024,
            batch_size=64,
            n_epochs=10,
            gamma=0.99,
            gae_lambda=0.95,
            clip_range=0.2,
            ent_coef=0.01,
            tensorboard_log=logs_dir,
            device="cpu"
        )
    else:
        print("🌱 Sıfırdan yeni yapay zeka ağı kuruluyor...")
        model = PPO(
            policy="MlpPolicy",
            env=env,
            learning_rate=3e-4,
            n_steps=1024,
            batch_size=64,
            n_epochs=10,
            gamma=0.99,
            gae_lambda=0.95,
            clip_range=0.2,
            ent_coef=0.01,
            verbose=0,
            tensorboard_log=logs_dir,
            policy_kwargs=policy_kwargs,
            device="cpu"  # Hızlı ve stabil CPU hesaplaması
        )

    # 4. Ara Kayıt (Checkpoint) Callback'i
    checkpoint_callback = CheckpointCallback(
        save_freq=2048,
        save_path=models_dir,
        name_prefix="robot_ppo_model"
    )

    visual_callback = TrainingVisualLogger()

    # Toplam Eğitim Adımı: 50.000 adım
    TOTAL_TIMESTEPS = 50_000

    print("🧠 Yapay Zeka Ağı Hazır.")
    print(f"🎯 Toplam Hedef Adım : {TOTAL_TIMESTEPS}")
    print("-" * 65)
    print("CANLI EĞİTİM BAŞLADI (Durdurmak için Ctrl+C yapabilirsiniz):\n")

    try:
        model.learn(
            total_timesteps=TOTAL_TIMESTEPS,
            callback=[checkpoint_callback, visual_callback],
            progress_bar=True,
            reset_num_timesteps=False
        )
        
        # En son modeli kaydet
        final_model_path = os.path.join(models_dir, "best_model.zip")
        model.save(final_model_path)
        print("\n" + "=" * 65)
        print(f"🎉 EĞİTİM TAMAMLANDI! En iyi model kaydedildi: {final_model_path}")
        print("=" * 65)

    except KeyboardInterrupt:
        print("\n⚠️ Eğitim durduruldu. Mevcut model güvenle kaydediliyor...")
        final_model_path = os.path.join(models_dir, "interrupted_model.zip")
        model.save(final_model_path)
        best_model_path = os.path.join(models_dir, "best_model.zip")
        model.save(best_model_path)
        print(f"💾 Model kaydedildi: {final_model_path} ve {best_model_path}")
    finally:
        env.close()

if __name__ == '__main__':
    main()
