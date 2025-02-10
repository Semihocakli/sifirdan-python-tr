"""
Renk Haritaları ve Isı Haritaları (Colormaps & Heatmaps)
--------------------------------------------------
Bu örnek, matplotlib ile renk haritaları ve ısı haritalarının nasıl oluşturulacağını gösterir.

Kullanım Alanları:
- Sıcaklık dağılımı görselleştirme
- Korelasyon matrislerinin analizi
- Yoğunluk haritaları
- Veri yoğunluğu analizi
- Örüntü tanıma ve görselleştirme

Özellikler:
- Özel renk haritaları
- Korelasyon matrisleri
- Açıklamalı ısı haritaları
- Renk ölçekleri
- Metin açıklamaları
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Özel renk haritası oluşturma
colors = ['darkred', 'red', 'orange', 'yellow', 'white']  # Renk listesi
n_bins = 100  # Renk sayısı
custom_cmap = LinearSegmentedColormap.from_list('custom', colors, N=n_bins)  # Özel renk haritası

# Isı haritası için veri oluşturma
data = np.random.normal(0, 1, (20, 20))  # Rastgele veri matrisi
correlation_matrix = np.corrcoef(data)  # Korelasyon matrisi

plt.figure(figsize=(15, 5))  # 15x5 inç boyutunda figür

# Temel ısı haritası
plt.subplot(131)  # 1. alt grafik
plt.imshow(data, cmap=custom_cmap)  # Özel renk haritası ile görselleştirme
plt.colorbar()  # Renk ölçeği ekleme
plt.title('Özel Renk Haritası')

# Korelasyon matrisi ısı haritası
plt.subplot(132)  # 2. alt grafik
im = plt.imshow(correlation_matrix, cmap='coolwarm')  # Korelasyon matrisini görselleştirme
plt.colorbar(im)  # Renk ölçeği ekleme
plt.title('Korelasyon Matrisi')

# Açıklamalı ısı haritası
plt.subplot(133)  # 3. alt grafik
small_data = np.random.randint(0, 100, size=(5, 5))  # 5x5 rastgele tamsayı matrisi
im = plt.imshow(small_data, cmap='YlOrRd')  # Sarı-Turuncu-Kırmızı renk haritası
plt.colorbar(im)  # Renk ölçeği ekleme

# Metin açıklamaları ekleme
for i in range(5):
    for j in range(5):
        text = plt.text(j, i, small_data[i, j],
                       ha="center", va="center", color="black")  # Hücre değerlerini ekle

plt.title('Açıklamalı Isı Haritası')
plt.tight_layout()  # Alt grafikler arası boşlukları otomatik ayarlama
plt.show()  # Grafiği göster 