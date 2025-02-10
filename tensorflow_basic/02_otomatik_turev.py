"""
TensorFlow Otomatik Türev Hesaplama (Autodiff)
------------------------------------------
TensorFlow'un en güçlü özelliklerinden biri, otomatik türev hesaplama yeteneğidir.
Bu özellik, derin öğrenme modellerinin eğitiminde gradyan hesaplamalarını otomatikleştirir.

Özellikler:
- Otomatik gradyan hesaplama
- Zincir kuralı uygulaması
- Verimli hesaplama
- Yüksek doğruluk
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 1. Basit Türev Örneği
print("1. Basit Türev Örneği:")
print("-" * 30)

x = tf.Variable(3.0)  # Değişken tanımlama

with tf.GradientTape() as tape:
    y = x * x  # y = x²

# dy/dx hesaplama
dy_dx = tape.gradient(y, x)
print("x = 3 için x²'nin türevi:", dy_dx.numpy())  # Beklenen: 2x = 6

# 2. Çoklu Değişken Türevi
print("\n2. Çoklu Değişken Türevi:")
print("-" * 30)

x = tf.Variable(2.0)
y = tf.Variable(3.0)

with tf.GradientTape() as tape:
    z = x**2 + y**2  # z = x² + y²

# dz/dx ve dz/dy hesaplama
gradients = tape.gradient(z, [x, y])
print("x = 2, y = 3 için gradyanlar:")
print("dz/dx:", gradients[0].numpy())  # Beklenen: 2x = 4
print("dz/dy:", gradients[1].numpy())  # Beklenen: 2y = 6

# 3. Görselleştirme ile Türev
print("\n3. Görselleştirme ile Türev:")
print("-" * 30)

# Fonksiyon: f(x) = x³ - 2x² + 2
x_noktalar = np.linspace(-2, 3, 100)
x_tensor = tf.constant(x_noktalar)

with tf.GradientTape() as tape:
    x_var = tf.Variable(x_tensor)
    y = x_var**3 - 2*x_var**2 + 2

# Türev hesaplama
dy_dx = tape.gradient(y, x_var)

# Görselleştirme
plt.figure(figsize=(10, 6))
plt.plot(x_noktalar, y.numpy(), label='f(x) = x³ - 2x² + 2')
plt.plot(x_noktalar, dy_dx.numpy(), label="f'(x) = 3x² - 4x")
plt.grid(True)
plt.legend()
plt.title('Fonksiyon ve Türevi')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 4. Yüksek Mertebeden Türevler
print("\n4. Yüksek Mertebeden Türevler:")
print("-" * 30)

x = tf.Variable(2.0)

with tf.GradientTape() as tape2:
    with tf.GradientTape() as tape1:
        y = x**3  # y = x³
    
    # Birinci türev: dy/dx = 3x²
    dy_dx = tape1.gradient(y, x)
    
# İkinci türev: d²y/dx² = 6x
d2y_dx2 = tape2.gradient(dy_dx, x)

print("x = 2 için:")
print("dy/dx:", dy_dx.numpy())    # Beklenen: 3x² = 12
print("d²y/dx²:", d2y_dx2.numpy())  # Beklenen: 6x = 12 