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

    # 3. PPO HİPERPARAMETRELERİ (ÖĞRENME AYARLARI)
    # -------------------------------------------------------------
    # learning_rate (Öğrenme Hızı - 3e-4): Ağın ağırlıklarını ne hızda güncelleyeceği.
    #   -> Çok büyük olursa öğrendiklerini unutur, çok küçük olursa çok yavaş öğrenir.
    #
    # n_steps (Tecrübe Toplama Adımı - 1024): Yapay zekanın her güncelleme öncesi
    #   çevreden topladığı adım (tecrübe) sayısı.
    #
    # batch_size (Mini Paket Boyutu - 64): 1024 adımlık tecrübeyi 64'lük paketler
    #   halinde nöral ağa besleyerek öğrenmeyi optimize eder.
    #
    # n_epochs (Tekrar Sayısı - 10): Toplanan verinin üzerinden kaç kez geçileceği.
    #
    # gamma (Gelecek İskonto Oranı - 0.99): Robotun anlık ödül yerine gelecekteki
    #   büyük hedefe ne kadar değer vereceği (1.0'a yakın = uzun vadeli planlama).
    #
    # gae_lambda (Avantaj Katsayısı - 0.95): Ödül tahminlerindeki varyansı düşürür.
    #
    # clip_range (PPO Politika Sınırı - 0.2): Yeni stratejinin eski stratejiden en fazla
    #   %20 farklılaşmasına izin verir. Bu PPO'nun en büyük güvenlik kilididir.
    #
    # ent_coef (Merak / Keşif Oranı - 0.01): Robotun rastgele yeni hareketler deneme
    #   istegi. Baştan yüksek merakla yeni şeyler keşfeder.
    # -------------------------------------------------------------

    policy_kwargs = dict(
        net_arch=dict(pi=[128, 128], vf=[128, 128])  # 2 Gizli katman, 128'er nöron
    )

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

    # Toplam Eğitim Adımı: 50.000 adım (Yaklaşık 15-20 dakika)
    TOTAL_TIMESTEPS = 50_000

    print("🧠 Yapay Zeka Ağı Kuruldu.")
    print(f"🎯 Toplam Eğitim Adımı : {TOTAL_TIMESTEPS}")
    print("-" * 65)
    print("CANLI EĞİTİM BAŞLADI (Durdurmak için Ctrl+C yapabilirsiniz):\n")

    try:
        model.learn(
            total_timesteps=TOTAL_TIMESTEPS,
            callback=[checkpoint_callback, visual_callback],
            progress_bar=True
        )
        
        # En son modeli kaydet
        final_model_path = os.path.join(models_dir, "best_model.zip")
        model.save(final_model_path)
        print("\n" + "=" * 65)
        print(f"🎉 EĞİTİM TAMAMLANDI! En iyi model kaydedildi: {final_model_path}")
        print("=" * 65)

    except KeyboardInterrupt:
        print("\n⚠️ Eğitim kullanıcı tarafından durduruldu. Mevcut model kaydediliyor...")
        final_model_path = os.path.join(models_dir, "interrupted_model.zip")
        model.save(final_model_path)
        print(f"💾 Model kaydedildi: {final_model_path}")
    finally:
        env.close()

if __name__ == '__main__':
    main()
