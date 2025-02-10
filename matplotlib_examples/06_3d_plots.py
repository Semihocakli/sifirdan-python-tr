"""
3 Boyutlu Grafikler (3D Plots)
---------------------------
Bu örnek, matplotlib ile 3 boyutlu grafiklerin nasıl oluşturulacağını gösterir.

Kullanım Alanları:
- Yüzey haritalaması
- Topografik görselleştirme
- Bilimsel simülasyonlar
- Matematiksel fonksiyonların 3B gösterimi
- Veri yoğunluğu analizi

Özellikler:
- Yüzey grafikleri (Surface plots)
- Tel kafes grafikleri (Wireframe plots)
- Renk haritası kullanımı
- 3B görünüm açısı kontrolü
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 3B grafik için veri oluşturma
x = np.linspace(-5, 5, 100)  # x ekseni verileri
y = np.linspace(-5, 5, 100)  # y ekseni verileri
X, Y = np.meshgrid(x, y)  # 2B ızgara oluşturma
Z = np.sin(np.sqrt(X**2 + Y**2))  # z ekseni verileri

# Grafik oluşturma
fig = plt.figure(figsize=(12, 5))  # 12x5 inç boyutunda figür

# Yüzey grafiği
ax1 = fig.add_subplot(121, projection='3d')  # 3B projeksiyon ile alt grafik
surf = ax1.plot_surface(X, Y, Z, cmap='viridis')  # Renkli yüzey grafiği
ax1.set_title('Yüzey Grafiği')
fig.colorbar(surf)  # Renk ölçeği ekleme

# Tel kafes grafiği
ax2 = fig.add_subplot(122, projection='3d')  # 3B projeksiyon ile alt grafik
ax2.plot_wireframe(X, Y, Z, rstride=5, cstride=5)  # Tel kafes grafiği
ax2.set_title('Tel Kafes Grafiği')

plt.tight_layout()  # Alt grafikler arası boşlukları otomatik ayarlama
plt.show()  # Grafiği göster 