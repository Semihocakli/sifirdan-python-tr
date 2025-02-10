"""
Çubuk ve Histogram Grafikleri (Bar Charts & Histograms)
---------------------------------------------------
Bu örnek, matplotlib ile çubuk grafikleri ve histogramların nasıl oluşturulacağını gösterir.

Kullanım Alanları:
Çubuk Grafikleri:
- Kategorik verilerin karşılaştırılması
- Satış verilerinin analizi
- Anket sonuçlarının görselleştirilmesi
- Performans karşılaştırmaları

Histogramlar:
- Veri dağılımının analizi
- Frekans dağılımlarının gösterimi
- İstatistiksel analizler
- Veri yoğunluğunun incelenmesi

Özellikler:
- Hata çubukları (error bars)
- Özelleştirilmiş renk ve kenar çizgileri
- Alt grafik (subplot) kullanımı
- Otomatik bin (sınıf) hesaplama
"""

import matplotlib.pyplot as plt
import numpy as np

# Çubuk grafik verileri
categories = ['A', 'B', 'C', 'D']  # Kategoriler
values = [23, 45, 56, 78]  # Her kategori için değerler
errors = [3, 5, 2, 4]  # Hata payları

plt.figure(figsize=(12, 5))  # 12x5 inç boyutunda figür

# Basit çubuk grafik
plt.subplot(121)  # 1. alt grafik
plt.bar(categories, values, yerr=errors, capsize=5)  # Hata çubuklu çubuk grafik
plt.title('Hata Çubuklu Çubuk Grafik')

# Histogram
plt.subplot(122)  # 2. alt grafik
data = np.random.normal(100, 15, 1000)  # Normal dağılımlı rastgele veri (ortalama=100, std=15)
plt.hist(data, bins=30, color='skyblue', edgecolor='black')  # 30 bölmeli histogram
plt.title('Histogram')
plt.xlabel('Değer')
plt.ylabel('Frekans')

plt.tight_layout()  # Alt grafikler arası boşlukları otomatik ayarlama
plt.show()  # Grafiği göster 