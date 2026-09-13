#!/usr/bin/env python3
"""
save_map.py
-----------
SLAM tarafından canlı olarak oluşturulan /map grid haritasını
my_robot_pkg/maps/house_map (.yaml ve .pgm) olarak kaydeder.
"""

import os
import subprocess
import sys

def main():
    package_maps_dir = os.path.expanduser('/home/onur/autonomous_robot/src/my_robot_pkg/maps')
    os.makedirs(package_maps_dir, exist_ok=True)
    map_filepath = os.path.join(package_maps_dir, 'house_map')

    print(f"\n[Harita Kaydedici] Canlı harita alınıyor ve kaydediliyor...")
    print(f"Hedef Dosya: {map_filepath}.yaml / {map_filepath}.pgm\n")

    cmd = [
        'ros2', 'run', 'nav2_map_server', 'map_saver_cli',
        '-f', map_filepath,
        '--ros-args', '-p', 'map_subscribe_transient_local:=true'
    ]

    try:
        res = subprocess.run(cmd, check=True)
        if res.returncode == 0:
            print("\n" + "="*50)
            print("✅ HARİTA BAŞARIYLA KAYDEDİLDİ!")
            print(f"Konum: {package_maps_dir}")
            print("="*50 + "\n")
    except Exception as e:
        print(f"\n❌ Harita kaydedilirken hata oluştu: {e}")
        print("Lütfen haritalama düğümünün (/map yayını) aktif olduğundan emin olun.\n")

if __name__ == '__main__':
    main()
