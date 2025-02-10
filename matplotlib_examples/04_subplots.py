"""
Alt Grafikler (Subplots)
----------------------
Bu örnek, matplotlib ile alt grafiklerin nasıl oluşturulacağını ve düzenleneceğini gösterir.

Kullanım Alanları:
- Farklı veri setlerinin karşılaştırmalı analizi
- Çoklu görselleştirme
- Farklı açılardan veri analizi
- Zaman serisi verilerinin çoklu gösterimi

Özellikler:
- 2x2 grid düzeninde alt grafikler
- Farklı matematiksel fonksiyonların gösterimi
- Her grafik için ayrı başlık ve eksen etiketleri
- Otomatik yerleşim düzenleme
"""

import matplotlib.pyplot as plt
import numpy as np

# Veri oluşturma
x = np.linspace(0, 10, 100)  # 0-10 arası 100 nokta
y1 = np.sin(x)  # Sinüs fonksiyonu
y2 = np.cos(x)  # Kosinüs fonksiyonu
y3 = np.tan(x)  # Tanjant fonksiyonu
y4 = x**2  # Karesel fonksiyon

# 2x2 alt grafik oluşturma
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))  # 12x10 inç boyutunda 4 alt grafik

# Grafik 1 - Sinüs
ax1.plot(x, y1)
ax1.set_title('Sinüs')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')

# Grafik 2 - Kosinüs
ax2.plot(x, y2, 'r-')
ax2.set_title('Kosinüs')
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')

# Grafik 3 - Tanjant
ax3.plot(x, y3, 'g-')
ax3.set_title('Tanjant')
ax3.set_xlabel('x')
ax3.set_ylabel('tan(x)')

# Grafik 4 - Karesel
ax4.plot(x, y4, 'm-')
ax4.set_title('Karesel')
ax4.set_xlabel('x')
ax4.set_ylabel('x²')

plt.tight_layout()  # Alt grafikler arası boşlukları otomatik ayarlama
plt.show()  # Grafiği göster 