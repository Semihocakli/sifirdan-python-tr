"""
Saçılım Grafikleri (Scatter Plots)
--------------------------------
Bu örnek, matplotlib ile saçılım grafiklerinin nasıl oluşturulacağını gösterir.

Kullanım Alanları:
- İki değişken arasındaki ilişkinin incelenmesi
- Korelasyon analizi
- Kümeleme çalışmaları
- Anomali tespiti
- Veri dağılımının görselleştirilmesi

Özellikler:
- Değişken boyutlu noktalar
- Renk haritası (colormap) kullanımı
- Farklı işaretçi stilleri
- Alt grafik (subplot) kullanımı
"""

import matplotlib.pyplot as plt
import numpy as np

# Rastgele veri oluşturma
np.random.seed(42)  # Tekrar üretilebilirlik için sabit tohum değeri
x = np.random.rand(50)  # 0-1 arası 50 rastgele x değeri
y = np.random.rand(50)  # 0-1 arası 50 rastgele y değeri
colors = np.random.rand(50)  # Noktaların renkleri için rastgele değerler
sizes = 1000 * np.random.rand(50)  # Noktaların boyutları için rastgele değerler

# Alt grafikleri içeren figür oluşturma
plt.figure(figsize=(12, 5))  # 12x5 inç boyutunda figür

# Temel saçılım grafiği
plt.subplot(121)  # 1. alt grafik
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')  # Saçılım grafiği çizimi
plt.colorbar()  # Renk ölçeği ekleme
plt.title('Değişken Boyut ve Renkte Saçılım Grafiği')

# Farklı işaretçi stilleri
plt.subplot(122)  # 2. alt grafik
markers = ['o', 's', '^', 'v', '<', '>', 'p', '*']  # Farklı işaretçi tipleri
for idx, marker in enumerate(markers):
    plt.scatter(x[idx::8], y[idx::8], marker=marker, label=f'İşaretçi {marker}')
plt.legend()  # Grafik açıklamalarını gösterme
plt.title('Farklı İşaretçi Stilleri')

plt.tight_layout()  # Alt grafikler arası boşlukları otomatik ayarlama
plt.show()  # Grafiği göster 