#!/usr/bin/env bash
set -euo pipefail

echo "====================================================="
echo "  Autonomous Robot - ROS 2 Kurulum Sihirbazı        "
echo "  Hedef Dağıtım: Ubuntu 26.04 (Resolute) -> ROS 2 Lyrical"
echo "====================================================="

# Root kontrolü
if [ "$EUID" -ne 0 ]; then
  echo "[HATA] Lütfen bu scripti sudo ile çalıştırın:"
  echo "       sudo bash scripts/install_ros2.sh"
  exit 1
fi

echo "[1/6] Sistem paketleri ve temel araçlar güncelleniyor..."
apt-get update
apt-get install -y software-properties-common curl gnupg lsb-release build-essential git

echo "[2/6] ROS 2 resmi GPG anahtarı ekleniyor..."
install -m 0755 -d /etc/apt/keyrings
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /tmp/ros.key
gpg --yes --dearmor -o /etc/apt/keyrings/ros-archive-keyring.gpg /tmp/ros.key
rm -f /tmp/ros.key

echo "[3/6] ROS 2 APT kaynak listesi yapılandırılıyor..."
UBUNTU_CODENAME=$(lsb_release -cs)
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu ${UBUNTU_CODENAME} main" > /etc/apt/sources.list.d/ros2.list

echo "[4/6] Paket listeleri yenileniyor..."
apt-get update

echo "[5/6] ROS 2 Lyrical Desktop ve geliştirme araçları kuruluyor..."
apt-get install -y \
  ros-lyrical-desktop \
  ros-lyrical-slam-toolbox \
  ros-lyrical-nav2-controller \
  ros-lyrical-nav2-bt-navigator \
  ros-lyrical-nav2-costmap-2d \
  ros-lyrical-nav2-amcl \
  ros-lyrical-nav2-map-server \
  ros-lyrical-nav2-behaviors \
  ros-lyrical-tf2-tools \
  ros-lyrical-teleop-twist-keyboard \
  ros-dev-tools \
  python3-colcon-common-extensions \
  python3-rosdep

echo "[6/6] rosdep başlatılıyor..."
if [ ! -f /etc/ros/rosdep/sources.list.d/20-default.list ]; then
  rosdep init || true
fi

# Normal kullanıcı (SUDO_USER) için bashrc ayarı
TARGET_USER="${SUDO_USER:-$USER}"
USER_HOME=$(eval echo "~${TARGET_USER}")

if [ -f "$USER_HOME/.bashrc" ]; then
  if ! grep -q "source /opt/ros/lyrical/setup.bash" "$USER_HOME/.bashrc"; then
    echo "" >> "$USER_HOME/.bashrc"
    echo "# ROS 2 Lyrical Environment" >> "$USER_HOME/.bashrc"
    echo "source /opt/ros/lyrical/setup.bash" >> "$USER_HOME/.bashrc"
    echo "[BİLGİ] $USER_HOME/.bashrc dosyasına ROS 2 ortam değişkeni eklendi."
  fi
fi

# rosdep update'i normal kullanıcı olarak çalıştır
if [ -n "${SUDO_USER:-}" ]; then
  sudo -u "$SUDO_USER" rosdep update || true
fi

echo "====================================================="
echo "  TEBRİKLER! ROS 2 Kurulumu Tamamlandı.             "
echo "  Test etmek için yeni bir terminalde:               "
echo "    ros2 topic list                                 "
echo "====================================================="
