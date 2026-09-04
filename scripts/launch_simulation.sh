#!/usr/bin/env bash
# ROS 2 ve Simülasyon Köprüsünü Başlatma Scripti
set -e

source /opt/ros/lyrical/setup.bash
if [ -f "/home/onur/autonomous_robot/ros2_ws/install/setup.bash" ]; then
    source /home/onur/autonomous_robot/ros2_ws/install/setup.bash
fi

echo "======================================================"
echo "  Autonomous Robot - ROS 2 Simülasyon Köprüsü Aktif   "
echo "  Sensörler: 720p Kamera, 4x HC-SR04, Odom, OLED      "
echo "======================================================"

# Simülasyon arka plan motorunu başlat
python3 /home/onur/autonomous_robot/AutonomousSim/Content/Python/robot_sim_bridge.py &
SIM_PID=$!

trap "kill $SIM_PID 2>/dev/null || true" EXIT

ros2 launch autonomous_robot_bridge bridge.launch.py
