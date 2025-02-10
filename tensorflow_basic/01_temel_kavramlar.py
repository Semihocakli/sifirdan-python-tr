"""
TensorFlow Temel Kavramlar
-------------------------
TensorFlow, Google tarafından geliştirilen açık kaynaklı bir makine öğrenimi kütüphanesidir.
Temel yapı taşı 'tensor' (çok boyutlu dizi) üzerine kuruludur.

Özellikler:
- Otomatik türev hesaplama
- GPU desteği
- Yüksek seviyeli API'ler
- Dağıtık hesaplama desteği
"""

import tensorflow as tf
import numpy as np

# TensorFlow sürümünü kontrol et
print("TensorFlow Sürümü:", tf.__version__)

# 1. Temel Tensör Oluşturma
print("\n1. Temel Tensör Örnekleri:")
print("-" * 30)

# Skaler (0-boyutlu tensör)
skaler = tf.constant(42)
print("Skaler:", skaler.numpy())

# Vektör (1-boyutlu tensör)
vektor = tf.constant([1, 2, 3, 4])
print("Vektör:", vektor.numpy())

# Matris (2-boyutlu tensör)
matris = tf.constant([[1, 2], [3, 4]])
print("Matris:\n", matris.numpy())

# 3-boyutlu tensör
tensor_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3B Tensör:\n", tensor_3d.numpy())

# 2. Tensör Özellikleri
print("\n2. Tensör Özellikleri:")
print("-" * 30)

print("Şekil (Shape):", matris.shape)
print("Veri Tipi:", matris.dtype)
print("Cihaz:", matris.device)  # CPU/GPU bilgisi

# 3. Tensör Oluşturma Yöntemleri
print("\n3. Tensör Oluşturma Yöntemleri:")
print("-" * 30)

# Sıfırlar matrisi
sifirlar = tf.zeros([2, 3])
print("Sıfırlar:\n", sifirlar.numpy())

# Birler matrisi
birler = tf.ones([2, 3])
print("Birler:\n", birler.numpy())

# Rastgele değerler
rastgele = tf.random.normal([2, 3])
print("Rastgele (Normal Dağılım):\n", rastgele.numpy())

# 4. Temel Tensör İşlemleri
print("\n4. Temel Tensör İşlemleri:")
print("-" * 30)

a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])

# Toplama
print("Toplama:\n", tf.add(a, b).numpy())

# Çarpma (element-wise)
print("Çarpma (Element-wise):\n", tf.multiply(a, b).numpy())

# Matris çarpımı
print("Matris Çarpımı:\n", tf.matmul(a, b).numpy())

# 5. NumPy ile Etkileşim
print("\n5. NumPy ile Etkileşim:")
print("-" * 30)

# NumPy dizisinden tensör oluşturma
np_dizi = np.array([[1, 2], [3, 4]])
tensor = tf.convert_to_tensor(np_dizi)
print("NumPy'dan Tensör:\n", tensor.numpy())

# Tensörden NumPy dizisi oluşturma
numpy_dizi = tensor.numpy()
print("Tensörden NumPy:\n", numpy_dizi) 