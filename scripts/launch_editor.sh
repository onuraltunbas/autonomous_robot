#!/usr/bin/env bash
# Unreal Engine 5 Projesini Editörde Başlatma Scripti
set -e

PROJECT_PATH="/home/onur/autonomous_robot/AutonomousSim/AutonomousSim.uproject"
UE_EDITOR="/home/onur/UnrealEngine/Engine/Binaries/Linux/UnrealEditor"

echo "================================================="
echo "  Unreal Engine 5 - AutonomousSim Başlatılıyor... "
echo "================================================="

if [ ! -f "$UE_EDITOR" ]; then
    echo "[HATA] UnrealEditor bulunamadı: $UE_EDITOR"
    exit 1
fi

exec "$UE_EDITOR" "$PROJECT_PATH" "$@"
