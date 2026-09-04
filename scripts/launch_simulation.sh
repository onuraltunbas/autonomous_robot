#!/usr/bin/env bash
# ROS 2 ve Köprü Düğümünü Başlatma Scripti
set -e

source /opt/ros/lyrical/setup.bash
if [ -f "/home/onur/autonomous_robot/ros2_ws/install/setup.bash" ]; then
    source /home/onur/autonomous_robot/ros2_ws/install/setup.bash
else
    echo "[UYARI] ros2_ws derleniyor..."
    cd /home/onur/autonomous_robot/ros2_ws && colcon build --symlink-install
    source /home/onur/autonomous_robot/ros2_ws/install/setup.bash
fi

echo "======================================================"
echo "  Autonomous Robot - ROS 2 Simülasyon Köprüsü Aktif   "
echo "  Tüm sensörler (Kamera, 4x Sonar, Odom, OLED) hazır  "
echo "======================================================"

ros2 launch autonomous_robot_bridge bridge.launch.py
