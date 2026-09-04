# Robot Kinematik ve Sensör Mimarisi Dokümantasyonu

Bu belge, Unreal Engine simülasyonunda ve ROS 2 mimarisinde kullanılacak 4 tekerlekli kompakt otonom robotun fiziksel, matematiksel ve kinematik temellerini tanımlar.

---

## 1. Fiziksel Ölçüler ve Şasi Geometrisi

* **Şasi Tipi:** Kutu (Prism) şasi
* **Gövde Boyutları:**
  * Uzunluk ($L_c$): $0.20\text{ m}$ ($20\text{ cm}$)
  * Genişlik ($W_c$): $0.20\text{ m}$ ($20\text{ cm}$)
  * Yükseklik ($H_c$): $0.05\text{ m}$ ($5\text{ cm}$)
* **Toplam Kütle:** Yaklaşık $1.6\text{ kg}$ (Şasi: $1.2\text{ kg}$, 4x Tekerlek: $0.1\text{ kg} \times 4$, Elektronik ve Sensörler)
* **Yerden Yükseklik (Ground Clearance):** $0.015\text{ m}$ - $0.020\text{ m}$ ($15-20\text{ mm}$)
* **Gövde Ağırlık Merkezi (CoM):** Şasinin geometrik merkezindedir $(x=0, y=0, z=0.045\text{ m})$.

---

## 2. Tekerlek ve Sürüş Kinematiği (4WD Skid-Steer / Differential Drive)

Robotumuz 4 adet DC motor ile her tekerleğin bağımsız kontrol edildiği **Skid-Steer (Kaymalı Yönlendirme / 4WD Diferansiyel)** mimarisine sahiptir.

### Temel Kinematik Parametreler
* **Tekerlek Yarıçapı ($r$):** $0.0325\text{ m}$ (Çap: $65\text{ mm}$)
* **Tekerlek Genişliği ($w$):** $0.025\text{ m}$ ($25\text{ mm}$)
* **Dingil Açıklığı / Wheelbase ($L$):** Ön ve arka akslar arası mesafe = $0.12\text{ m}$ ($12\text{ cm}$)
  * Ön tekerlekler: $x = +0.06\text{ m}$
  * Arka tekerlekler: $x = -0.06\text{ m}$
* **Tekerlek İzi Genişliği / Track Width ($W$):** Sol ve sağ tekerlek temas noktaları arası mesafe = $0.225\text{ m}$ ($22.5\text{ cm}$)
  * Sol tekerlekler: $y = +0.1125\text{ m}$
  * Sağ tekerlekler: $y = -0.1125\text{ m}$

### Kinematik Denklemler

Robotun çizgisel hızı $v_x$ ($\text{m/s}$) ve açısal dönüş hızı $\omega_z$ ($\text{rad/s}$) olduğunda:

#### Ters Kinematik (Twist $\rightarrow$ Tekerlek Açısal Hızları):
Sol ve sağ tekerlek gruplarının açısal hızları ($\omega_L, \omega_R$):

$$\omega_L = \frac{v_x - \omega_z \cdot \frac{W_{eff}}{2}}{r}$$

$$\omega_R = \frac{v_x + \omega_z \cdot \frac{W_{eff}}{2}}{r}$$

* $W_{eff} = \chi \cdot W$: Skid-steer sistemlerde tekerleklerin dönüş esnasında zemine sürtünerek kaymasından (skidding) kaynaklanan efektif tekerlek izi katsayısıdır ($\chi \approx 1.1 - 1.3$).

#### İleri Kinematik (Odometri Hesaplama):
Tekerlek hızlarından robotun anlık hızı:

$$v_x = r \cdot \frac{\omega_R + \omega_L}{2}$$

$$\omega_z = r \cdot \frac{\omega_R - \omega_L}{W_{eff}}$$

---

## 3. Sensör Yerleşimleri ve Koordinat Çerçeveleri (TF Tree)

REP-105 standartlarına uygun koordinat hiyerarşisi:
`map` $\rightarrow$ `odom` $\rightarrow$ `base_footprint` $\rightarrow$ `base_link`

```
base_footprint (Z=0, zemin seviyesi)
  └── base_link (Z=0.045m, gövde merkezi)
        ├── wheel_front_left_link  (xyz: [0.06, 0.1125, -0.0125])
        ├── wheel_front_right_link (xyz: [0.06, -0.1125, -0.0125])
        ├── wheel_rear_left_link   (xyz: [-0.06, 0.1125, -0.0125])
        ├── wheel_rear_right_link  (xyz: [-0.06, -0.1125, -0.0125])
        │
        ├── camera_link (xyz: [0.085, 0.0, 0.055], pitch: 7° aşağı)
        │     └── camera_optical_link (REP-103: Z ileri, X sağ, Y aşağı)
        │
        ├── sonar_hub_link (xyz: [0.0, 0.0, 0.025])
        │     ├── sonar_front_link (Yaw: 0°, Ön)
        │     ├── sonar_left_link  (Yaw: +90°, Sol)
        │     ├── sonar_back_link  (Yaw: 180°, Arka)
        │     └── sonar_right_link (Yaw: -90°, Sağ)
        │
        └── nodemcu_link (xyz: [-0.055, 0.0, 0.026])
```

### A. 4x HC-SR04 Ultrasonik Sensör Dizilimi
* **Konum:** Robotun tam merkezinde üst yüzeyde 4 yöne (0°, 90°, 180°, 270°) bakan özel montaj bloğu.
* **Özellikler:**
  * Algılama Açısı (FOV): $15^\circ - 30^\circ$ konik alan
  * Ölçüm Aralığı: $0.02\text{ m}$ - $4.00\text{ m}$
  * ROS 2 Mesaj Türü: `sensor_msgs/msg/Range`
  * Topic İsimleri:
    * `/sensors/sonar_front`
    * `/sensors/sonar_left`
    * `/sensors/sonar_back`
    * `/sensors/sonar_right`

### B. 720p Harici Webcam Modeli
* **Konum:** Robotun ön üst kenarında ($x = +0.085\text{ m}$, $z = +0.055\text{ m}$), hafif öne eğimli ($7^\circ$).
* **Gerekçe:** Hem ilerideki engelleri hem de robotun hemen önündeki zemin bölgesini görerek Visual SLAM (RTAB-Map) ve engel algılama için kör noktayı minimuma indirir.
* **Özellikler:**
  * Çözünürlük: $1280 \times 720$ piksel (720p HD)
  * Yatay Görüş Açısı (HFOV): $\approx 65^\circ - 70^\circ$
  * FPS: $30\text{ fps}$
  * ROS 2 Mesaj Türleri:
    * `sensor_msgs/msg/Image` (`/camera/image_raw`)
    * `sensor_msgs/msg/CameraInfo` (`/camera/camera_info`)

### C. NodeMCU & OLED Ekran
* **Konum:** Robotun üst plakasında arka tarafa yakın ($x = -0.055\text{ m}$).
* **Ekran:** $0.96"$ SSD1306 OLED ($128 \times 64$ piksel, I2C).
* **Görev:**
  * Wi-Fi / IP adresi durumu
  * Batarya yüzdesi ve simülasyon FPS
  * 4 ultrasonik sensörün anlık cm mesafeleri
  * Otonom mod durumu (Nav2 NAVIGATING, IDLE, ERROR)
