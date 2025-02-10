"""
Coğrafi Grafikler (Geographic Plots)
--------------------------------
Bu örnek, matplotlib ile coğrafi verilerin nasıl görselleştirileceğini gösterir.

Kullanım Alanları:
- Konum bazlı veri analizi
- Nüfus yoğunluğu haritaları
- Bölgesel analiz ve görselleştirme
- Coğrafi dağılım analizi
- Bölge sınırlarının gösterimi

Özellikler:
- Enlem-boylam grafikleri
- Özel bölge görselleştirme
- Boyut tabanlı nokta gösterimi
- Izgara çizgileri
- Çoklu görselleştirme
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle

# Harita benzeri görselleştirme oluşturma
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))  # 15x6 inç boyutunda figür

# Coğrafi noktalar için saçılım grafiği
np.random.seed(42)  # Tekrar üretilebilirlik için sabit tohum
lats = np.random.uniform(30, 50, 50)  # Rastgele enlemler
lons = np.random.uniform(-120, -70, 50)  # Rastgele boylamlar
populations = np.random.uniform(100, 1000, 50)  # Rastgele nüfus değerleri

ax1.scatter(lons, lats, s=populations/10, alpha=0.6, 
           c=populations, cmap='viridis')  # Nüfusa göre boyutlandırılmış noktalar
ax1.set_xlabel('Boylam')
ax1.set_ylabel('Enlem')
ax1.set_title('Coğrafi Nokta Verileri')
ax1.grid(True)  # Izgara çizgilerini göster

# Özel bölge görselleştirme fonksiyonu
def draw_region(ax, center, size, color):
    circle = Circle(center, size, fill=False, color=color)  # Daire çiz
    ax.add_patch(circle)
    rect = Rectangle((center[0]-size/2, center[1]-size/2), 
                    size, size, fill=False, color=color)  # Kare çiz
    ax.add_patch(rect)

# Örnek bölgeler ekleme
centers = [(0, 0), (1, 1), (-1, -1)]  # Bölge merkezleri
sizes = [0.5, 0.7, 0.3]  # Bölge boyutları
colors = ['red', 'blue', 'green']  # Bölge renkleri

for center, size, color in zip(centers, sizes, colors):
    draw_region(ax2, center, size, color)  # Her bölgeyi çiz

ax2.set_xlim(-2, 2)  # x ekseni limitleri
ax2.set_ylim(-2, 2)  # y ekseni limitleri
ax2.set_title('Özel Bölge Görselleştirmesi')
ax2.grid(True)  # Izgara çizgilerini göster

plt.tight_layout()  # Alt grafikler arası boşlukları otomatik ayarlama
plt.show()  # Grafiği göster 