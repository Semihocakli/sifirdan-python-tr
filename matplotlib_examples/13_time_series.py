"""
Zaman Serisi Grafikleri (Time Series Plots)
--------------------------------------
Bu örnek, matplotlib ile zaman serisi verilerinin nasıl görselleştirileceğini gösterir.

Kullanım Alanları:
- Borsa ve finansal veri analizi
- Trend analizi
- Sıcaklık değişimi takibi
- Satış verilerinin zaman bazlı analizi
- Sensör verilerinin görselleştirilmesi

Özellikler:
- Temel zaman serisi grafikleri
- Mum grafiği (Candlestick)
- Trend gösterimi
- Dolgu alanları
- Renkli gösterimler
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Zaman serisi verisi oluşturma
dates = [datetime.now() + timedelta(days=x) for x in range(100)]  # 100 günlük tarih
values = np.cumsum(np.random.randn(100)) + 100  # Rastgele değerler

plt.figure(figsize=(15, 10))  # 15x10 inç boyutunda figür

# Temel zaman serisi
plt.subplot(211)  # 1. alt grafik
plt.plot(dates, values, 'b-', label='Değer')  # Çizgi grafiği
plt.fill_between(dates, values, min(values), alpha=0.1)  # Alt alanı doldur
plt.title('Trendli Zaman Serisi')
plt.legend()
plt.grid(True)  # Izgara çizgilerini göster

# Mum grafiği benzeri gösterim
plt.subplot(212)  # 2. alt grafik
opens = values[:-1]  # Açılış değerleri
closes = values[1:]  # Kapanış değerleri
highs = np.maximum(opens, closes) + np.random.rand(99)  # En yüksek değerler
lows = np.minimum(opens, closes) - np.random.rand(99)  # En düşük değerler

# Yükseliş (yeşil) ve düşüş (kırmızı) renklerini belirle
colors = ['green' if close >= open else 'red' 
          for open, close in zip(opens, closes)]

# Mum çubukları çiz
for i in range(len(opens)):
    plt.vlines(dates[i], lows[i], highs[i], 
               color=colors[i], linewidth=1)  # Gölge çizgisi
    plt.vlines(dates[i], opens[i], closes[i], 
               color=colors[i], linewidth=4)  # Mum gövdesi

plt.title('Mum Grafiği')
plt.grid(True)  # Izgara çizgilerini göster

plt.tight_layout()  # Alt grafikler arası boşlukları otomatik ayarlama
plt.show()  # Grafiği göster 