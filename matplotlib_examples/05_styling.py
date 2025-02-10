"""
Grafik Stillendirme (Plot Styling)
-------------------------------
Bu örnek, matplotlib ile grafiklerin nasıl özelleştirileceğini ve profesyonel görünüm kazandırılacağını gösterir.

Kullanım Alanları:
- Akademik yayınlar için grafik hazırlama
- Sunum ve raporlar için görselleştirme
- Kurumsal raporlama
- Veri gazeteciliği

Özellikler:
- Hazır stil şablonları kullanımı (ggplot)
- Özel çizgi kalınlıkları ve renkleri
- Kenarlık özelleştirme
- Yarı saydam dolgu alanları
- Özelleştirilmiş ızgara çizgileri
- Profesyonel font boyutları ve etiketler
"""

import matplotlib.pyplot as plt
import numpy as np

# Stil ayarlama
plt.style.use('ggplot')  # ggplot stilini kullan

# Veri oluşturma
x = np.linspace(0, 10, 100)  # 0-10 arası 100 nokta
y = np.sin(x)  # Sinüs fonksiyonu

# Özel stilli grafik oluşturma
fig, ax = plt.subplots(figsize=(10, 6))  # 10x6 inç boyutunda grafik

# Özel stillerle çizim
ax.plot(x, y, 'b-', linewidth=2, label='sin(x)')  # Mavi, kalın çizgi
ax.fill_between(x, y, alpha=0.3)  # Eğri altını doldurma

# Eksenleri özelleştirme
ax.set_title('Özel Stilli Grafik Örneği', fontsize=16, pad=20)  # Başlık
ax.set_xlabel('X-ekseni', fontsize=12)  # x ekseni etiketi
ax.set_ylabel('Y-ekseni', fontsize=12)  # y ekseni etiketi

# Özel stilli ızgara ekleme
ax.grid(True, linestyle='--', alpha=0.7)  # Kesikli çizgili, yarı saydam ızgara

# Kenarlıkları özelleştirme
ax.spines['top'].set_visible(False)  # Üst kenarlığı gizle
ax.spines['right'].set_visible(False)  # Sağ kenarlığı gizle

# Açıklama ekleme
ax.legend(frameon=True, facecolor='white', framealpha=1)  # Beyaz arkaplanla açıklama kutusu

plt.show()  # Grafiği göster 