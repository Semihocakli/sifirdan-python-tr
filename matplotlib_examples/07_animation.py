"""
Animasyonlu Grafikler (Animated Plots)
----------------------------------
Bu örnek, matplotlib ile hareketli/animasyonlu grafiklerin nasıl oluşturulacağını gösterir.

Kullanım Alanları:
- Dinamik veri görselleştirme
- Zaman içindeki değişimlerin gösterimi
- Fizik simülasyonları
- Matematiksel fonksiyonların dinamik gösterimi
- Eğitim amaçlı animasyonlar

Özellikler:
- Gerçek zamanlı animasyon
- Kare hızı kontrolü
- Döngüsel hareket
- Etkileşimli görselleştirme
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Grafik ve eksen oluşturma
fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)  # 0-2π arası 100 nokta
line, = ax.plot(x, np.sin(x))  # Başlangıç sinüs dalgası

# Animasyon güncelleme fonksiyonu
def animate(frame):
    line.set_ydata(np.sin(x + frame/10.0))  # Her karede sinüs dalgasını kaydır
    return line,

# Animasyon oluşturma
ani = animation.FuncAnimation(
    fig, animate, frames=100,  # 100 kare
    interval=50, blit=True  # 50ms aralıklarla, hızlı çizim
)

ax.set_xlim(0, 2*np.pi)  # x ekseni limitleri
ax.set_ylim(-1.1, 1.1)  # y ekseni limitleri
plt.title('Hareketli Sinüs Dalgası')  # Başlık
plt.show()  # Grafiği göster 