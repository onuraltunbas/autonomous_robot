#!/usr/bin/env bash
# Webots Simülasyonunu ve Robot Dünyasını Başlatma Scripti
set -e

source /opt/ros/lyrical/setup.bash
if [ -f "/home/onur/autonomous_robot/ros2_ws/install/setup.bash" ]; then
    source /home/onur/autonomous_robot/ros2_ws/install/setup.bash
fi

export WEBOTS_HOME="/home/onur/webots"
export LD_LIBRARY_PATH="$WEBOTS_HOME/lib/controller:${LD_LIBRARY_PATH:-}"
export PYTHONPATH="$WEBOTS_HOME/lib/controller/python:${PYTHONPATH:-}"

WORLD_FILE="/home/onur/autonomous_robot/webots_project/worlds/apartment.wbt"

echo "======================================================"
echo "  Webots - 4WD Otonom Robot Simülasyonu Başlatılıyor "
echo "  Harita: Mobilyalı & Odalı Apartman Dünyası          "
echo "  Sensörler: 720p Kamera, 4x HC-SR04, OLED, 4WD DC   "
echo "======================================================"

exec "$WEBOTS_HOME/webots" "$WORLD_FILE" "$@"
