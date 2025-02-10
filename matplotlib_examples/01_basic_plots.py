"""
Temel Çizgi Grafikleri (Line Plots)
----------------------------------
Bu örnek, matplotlib ile temel çizgi grafiklerinin nasıl oluşturulacağını gösterir.

Kullanım Alanları:
- Zaman serisi verilerinin görselleştirilmesi
- Matematiksel fonksiyonların gösterimi
- Sürekli verilerin değişiminin analizi
- Trend analizi ve tahmin çalışmaları

Özellikler:
- Çoklu çizgi grafikleri
- Özelleştirilmiş eksen etiketleri
- Otomatik gösterge (legend)
- Izgara çizgileri
"""

import matplotlib.pyplot as plt
import numpy as np

# Veri oluşturma - 0'dan 10'a kadar 100 nokta
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Temel çizgi grafiği oluşturma
plt.figure(figsize=(10, 6))  # Grafik boyutunu ayarlama (10x6 inç)
plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-')  # Sinüs eğrisi
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--')  # Kosinüs eğrisi

# Grafik özelliklerini özelleştirme
plt.title('Temel Çizgi Grafiği')  # Başlık ekleme
plt.xlabel('x-ekseni')  # x ekseni etiketi
plt.ylabel('y-ekseni')  # y ekseni etiketi
plt.legend()  # Grafik açıklamalarını gösterme
plt.grid(True)  # Izgara ekle

plt.show()  # Grafiği göster 