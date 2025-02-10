"""
İstatistiksel Grafikler (Statistical Plots)
--------------------------------------
Bu örnek, matplotlib ile istatistiksel grafiklerin nasıl oluşturulacağını gösterir.

Kullanım Alanları:
- Veri dağılımlarının analizi
- Aykırı değerlerin tespiti
- Veri setlerinin karşılaştırılması
- Güven aralıklarının görselleştirilmesi
- İstatistiksel analizler

Özellikler:
- Kutu grafikleri (Box plots)
- Keman grafikleri (Violin plots)
- 2B yoğunluk grafikleri
- Güven elipsleri
- Çoklu veri seti karşılaştırma
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# Çoklu veri setleri oluşturma
np.random.seed(42)  # Tekrar üretilebilirlik için sabit tohum
data1 = np.random.normal(0, 1, 1000)  # Normal dağılımlı ilk veri seti
data2 = np.random.normal(2, 1.5, 1000)  # Normal dağılımlı ikinci veri seti

plt.figure(figsize=(15, 5))  # 15x5 inç boyutunda figür

# Kutu Grafiği
plt.subplot(131)  # 1. alt grafik
plt.boxplot([data1, data2], labels=['Veri 1', 'Veri 2'])
plt.title('Kutu Grafiği')

# Keman Grafiği
plt.subplot(132)  # 2. alt grafik
plt.violinplot([data1, data2])
plt.title('Keman Grafiği')

# 2B Yoğunluk Grafiği ve güven elipsleri
ax = plt.subplot(133)  # 3. alt grafik
x = np.random.normal(0, 1, 1000)  # x ekseni verileri
y = x * 0.5 + np.random.normal(0, 0.5, 1000)  # y ekseni verileri

# Yoğunluk grafiği çizimi
plt.scatter(x, y, alpha=0.5)  # Saçılım noktaları

# Güven elipslerini ekle
cov = np.cov(x, y)  # Kovaryans matrisi
lambda_, v = np.linalg.eig(cov)  # Özdeğer ve özvektörler
angle = np.degrees(np.arctan2(v[1, 0], v[0, 0]))  # Elips açısı

# Farklı standart sapma seviyeleri için elipsler
for n_std in [1, 2, 3]:
    ellipse = Ellipse(xy=(np.mean(x), np.mean(y)),
                      width=lambda_[0]**0.5 * n_std * 2,
                      height=lambda_[1]**0.5 * n_std * 2,
                      angle=angle,
                      facecolor='none',
                      edgecolor='red',
                      alpha=0.3)
    ax.add_patch(ellipse)

plt.title('2B Yoğunluk ve\nGüven Elipsleri')
plt.tight_layout()  # Alt grafikler arası boşlukları otomatik ayarlama
plt.show()  # Grafiği göster 