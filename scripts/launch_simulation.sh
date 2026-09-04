#!/usr/bin/env bash
# ROS 2 ve Unreal Engine Canlı Simülasyon Köprüsü
set -e

source /opt/ros/lyrical/setup.bash
if [ -f "/home/onur/autonomous_robot/ros2_ws/install/setup.bash" ]; then
    source /home/onur/autonomous_robot/ros2_ws/install/setup.bash
fi

echo "======================================================"
echo "  Autonomous Robot - ROS 2 Simülasyon Köprüsü Aktif   "
echo "  Unreal Engine Canlı Bağlantısı Bekleniyor (9876)... "
echo "======================================================"

ros2 launch autonomous_robot_bridge bridge.launch.py
