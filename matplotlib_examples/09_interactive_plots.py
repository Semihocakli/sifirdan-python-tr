"""
Etkileşimli Grafikler (Interactive Plots)
-------------------------------------
Bu örnek, matplotlib ile etkileşimli grafiklerin nasıl oluşturulacağını gösterir.

Kullanım Alanları:
- Parametre değişimlerinin anlık gözlemlenmesi
- Eğitim ve öğretim materyalleri
- Veri keşfi ve analizi
- Simülasyon kontrolleri
- Kullanıcı etkileşimli veri görselleştirme

Özellikler:
- Kaydırma çubukları (sliders)
- Gerçek zamanlı güncelleme
- Parametre kontrolü
- Dinamik veri görselleştirme
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons

# Veri oluşturma
t = np.linspace(0, 10, 1000)  # Zaman dizisi
initial_freq = 3.0  # Başlangıç frekansı
initial_amp = 1.0  # Başlangıç genliği

# Grafik ve çizim oluşturma
fig, ax = plt.subplots(figsize=(10, 6))  # 10x6 inç boyutunda grafik
line, = ax.plot(t, initial_amp * np.sin(2 * np.pi * initial_freq * t))  # Sinüs dalgası
ax.set_xlabel('Zaman')  # x ekseni etiketi
ax.set_ylabel('Genlik')  # y ekseni etiketi

# Kaydırma çubukları ekleme
ax_freq = plt.axes([0.2, 0.02, 0.6, 0.03])  # Frekans kontrolü için konum
ax_amp = plt.axes([0.2, 0.06, 0.6, 0.03])  # Genlik kontrolü için konum
freq_slider = Slider(ax_freq, 'Frekans', 0.1, 10.0, valinit=initial_freq)  # Frekans kontrolü
amp_slider = Slider(ax_amp, 'Genlik', 0.1, 2.0, valinit=initial_amp)  # Genlik kontrolü

# Güncelleme fonksiyonu
def update(val):
    freq = freq_slider.val  # Güncel frekans değeri
    amp = amp_slider.val  # Güncel genlik değeri
    line.set_ydata(amp * np.sin(2 * np.pi * freq * t))  # Grafiği güncelle
    fig.canvas.draw_idle()  # Yeniden çiz

# Kaydırma çubuklarına güncelleme fonksiyonunu bağla
freq_slider.on_changed(update)
amp_slider.on_changed(update)

plt.show()  # Grafiği göster 