# Autonomous Robot (Unreal Engine & ROS 2 Simulation)

Bu proje, Unreal Engine ortamında simüle edilen 4 tekerlekli, kompakt ve otonom bir mobil robot projesidir.

## Donanım ve Teknik Özellikler (Simülasyon Modeli)
- **Şasi / Gövde:** 20 cm (Genişlik) x 20 cm (Uzunluk) x 5 cm (Yükseklik) kompakt kutu tasarımı.
- **Sürüş Sistemi:** 4 tekerlekten bağımsız DC motor tahriki (4WD / Skid-Steer diferansiyel sürüş).
- **Kamera (Görsel Algılama):** En optimal görüş açısı için robotun ön üst tarafına konumlandırılmış 720p harici USB webcam modeli.
- **Mesafe Sensörleri:** Gövdenin tam merkezinde her biri ana yönlere (Ön, Arka, Sol, Sağ) bakan 4x HC-SR04 ultrasonik mesafe sensörü dizilimi.
- **Kontrol Ünitesi:** OLED ekranlı NodeMCU geliştirme kartı (telemetri, durum göstergesi ve motor sürücü köprüsü).
- **Yazılım Mimarisi:** ROS 2 (Nav2, Cartographer / RTAB-Map SLAM).
- **Simülasyon:** Unreal Engine.

## Proje Yol Haritası
1. Sistem ve Gereksinimlerin Hazırlanması (Ubuntu, ROS 2, UE entegrasyonu)
2. Robotun 3D / URDF ve Fiziksel Kinematik Modeli
3. Unreal Engine Ortamı ve Robot Aktörünün Oluşturulması
4. Sensör Entegrasyonu (720p Kamera yayını + 4x HC-SR04 mesafe verileri)
5. ROS 2 Haberleşme Köprüsü (Drives, TF, Odom, Sensor topics)
6. Haritalama (SLAM) ve Otonom Navigasyon (Nav2)
