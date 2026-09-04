#!/usr/bin/env bash
# Özel 4WD Robot Teleop Kontrolcüsünü Başlatma Scripti
set -e

source /opt/ros/lyrical/setup.bash
if [ -f "/home/onur/autonomous_robot/ros2_ws/install/setup.bash" ]; then
    source /home/onur/autonomous_robot/ros2_ws/install/setup.bash
fi

python3 /home/onur/autonomous_robot/ros2_ws/src/autonomous_robot_bridge/autonomous_robot_bridge/teleop_robot.py
