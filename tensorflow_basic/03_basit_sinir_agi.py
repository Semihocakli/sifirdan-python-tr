"""
TensorFlow ile Basit Sinir Ağı
--------------------------
TensorFlow'un Keras API'si ile basit bir sinir ağı modeli oluşturup eğiteceğiz.
Bu örnekte, el yazısı rakamları tanıma problemi (MNIST) üzerinde çalışacağız.

Özellikler:
- Keras Sequential API kullanımı
- Katman türleri
- Model eğitimi
- Performans değerlendirme
- Görselleştirme
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 1. Veri Setini Yükle
print("1. Veri Seti Yükleniyor...")
print("-" * 30)

# MNIST veri setini yükle
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Veriyi normalize et (0-1 arasına ölçekle)
x_train = x_train / 255.0
x_test = x_test / 255.0

print("Eğitim seti boyutu:", x_train.shape)
print("Test seti boyutu:", x_test.shape)

# 2. Model Oluşturma
print("\n2. Model Oluşturuluyor...")
print("-" * 30)

model = tf.keras.Sequential([
    # Girdi katmanı: Resimleri düzleştir (28x28 -> 784)
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    
    # Gizli katman 1: 128 nöron, ReLU aktivasyon
    tf.keras.layers.Dense(128, activation='relu'),
    
    # Seyreltme katmanı: Aşırı öğrenmeyi önlemek için
    tf.keras.layers.Dropout(0.2),
    
    # Gizli katman 2: 64 nöron, ReLU aktivasyon
    tf.keras.layers.Dense(64, activation='relu'),
    
    # Çıktı katmanı: 10 nöron (0-9 rakamları için)
    tf.keras.layers.Dense(10, activation='softmax')
])

# Model özetini göster
model.summary()

# 3. Model Derleme
print("\n3. Model Derleniyor...")
print("-" * 30)

model.compile(
    optimizer='adam',              # Optimizer algoritması
    loss='sparse_categorical_crossentropy',  # Kayıp fonksiyonu
    metrics=['accuracy']           # Metrikler
)

# 4. Model Eğitimi
print("\n4. Model Eğitiliyor...")
print("-" * 30)

history = model.fit(
    x_train, y_train,
    epochs=5,                # Eğitim turu sayısı
    batch_size=32,          # Her adımdaki örnek sayısı
    validation_split=0.2    # %20 doğrulama seti
)

# 5. Model Değerlendirme
print("\n5. Model Değerlendiriliyor...")
print("-" * 30)

test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test doğruluğu: {test_accuracy:.4f}")

# 6. Eğitim Sürecini Görselleştirme
print("\n6. Eğitim Süreci Görselleştiriliyor...")
print("-" * 30)

plt.figure(figsize=(12, 4))

# Doğruluk grafiği
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Eğitim')
plt.plot(history.history['val_accuracy'], label='Doğrulama')
plt.title('Model Doğruluğu')
plt.xlabel('Epoch')
plt.ylabel('Doğruluk')
plt.legend()

# Kayıp grafiği
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Eğitim')
plt.plot(history.history['val_loss'], label='Doğrulama')
plt.title('Model Kaybı')
plt.xlabel('Epoch')
plt.ylabel('Kayıp')
plt.legend()

plt.tight_layout()
plt.show()

# 7. Tahmin Örnekleri
print("\n7. Tahmin Örnekleri Görselleştiriliyor...")
print("-" * 30)

# Rastgele 5 örnek seç ve tahmin et
ornek_sayisi = 5
rastgele_indeksler = np.random.randint(0, len(x_test), ornek_sayisi)

plt.figure(figsize=(15, 3))
for i, idx in enumerate(rastgele_indeksler):
    # Tahmin yap
    tahmin = model.predict(x_test[idx:idx+1])
    tahmin_rakam = np.argmax(tahmin)
    
    # Görselleştir
    plt.subplot(1, ornek_sayisi, i+1)
    plt.imshow(x_test[idx], cmap='gray')
    plt.title(f'Tahmin: {tahmin_rakam}\nGerçek: {y_test[idx]}')
    plt.axis('off')

plt.tight_layout()
plt.show() 