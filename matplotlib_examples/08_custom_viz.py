"""
Özel Görselleştirmeler (Custom Visualizations)
-----------------------------------------
Bu örnek, matplotlib ile özel grafik türlerinin nasıl oluşturulacağını gösterir.

Kullanım Alanları:
- Kutupsal koordinat sisteminde veri gösterimi
- Radar/Örümcek grafikleri ile çok boyutlu veri analizi
- Performans karşılaştırma
- Döngüsel verilerin görselleştirilmesi
- Yön ve açı bazlı analizler

Özellikler:
- Kutupsal koordinat sistemi
- Radar grafikleri
- Açısal veri gösterimi
- Çokgen şeklinde veri görselleştirme
"""

import matplotlib.pyplot as plt
import numpy as np

# Grafik oluşturma
plt.figure(figsize=(12, 5))  # 12x5 inç boyutunda figür

# Kutupsal grafik
plt.subplot(121, projection='polar')  # Kutupsal koordinat sistemi
theta = np.linspace(0, 2*np.pi, 100)  # Açı değerleri
r = 2*np.cos(4*theta)  # Yarıçap değerleri
plt.plot(theta, r)
plt.title('Kutupsal Grafik')

# Özel görselleştirme (Radar grafiği)
plt.subplot(122)
categories = ['A', 'B', 'C', 'D', 'E']  # Kategoriler
values = [4, 3, 5, 2, 4]  # Değerler
angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)  # Kategori açıları
values = np.concatenate((values, [values[0]]))  # Çokgeni tamamla
angles = np.concatenate((angles, [angles[0]]))  # Çokgeni tamamla

ax = plt.subplot(122, projection='polar')  # Kutupsal koordinat sistemi
ax.plot(angles, values)  # Çizgileri çiz
ax.fill(angles, values, alpha=0.25)  # İç alanı doldur
ax.set_xticks(angles[:-1])  # Açı etiketlerini ayarla
ax.set_xticklabels(categories)  # Kategori isimlerini yerleştir
plt.title('Radar Grafiği')

plt.tight_layout()  # Alt grafikler arası boşlukları otomatik ayarlama
plt.show()  # Grafiği göster 