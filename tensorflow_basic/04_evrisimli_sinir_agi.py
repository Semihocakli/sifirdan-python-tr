"""
TensorFlow ile Evrişimli Sinir Ağı (CNN)
------------------------------------
Evrişimli Sinir Ağları, özellikle görüntü işleme problemlerinde çok başarılıdır.
Bu örnekte, MNIST veri seti üzerinde bir CNN modeli oluşturup eğiteceğiz.

Özellikler:
- Evrişim katmanları
- Havuzlama katmanları
- Tam bağlantılı katmanlar
- Görselleştirme ve analiz
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 1. Veri Setini Yükle ve Hazırla
print("1. Veri Seti Hazırlanıyor...")
print("-" * 30)

# MNIST veri setini yükle
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Veriyi yeniden boyutlandır (28x28x1 - gri tonlamalı görüntü)
x_train = x_train.reshape((60000, 28, 28, 1))
x_test = x_test.reshape((10000, 28, 28, 1))

# Veriyi normalize et
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

print("Eğitim seti boyutu:", x_train.shape)
print("Test seti boyutu:", x_test.shape)

# 2. CNN Modelini Oluştur
print("\n2. CNN Modeli Oluşturuluyor...")
print("-" * 30)

model = tf.keras.Sequential([
    # İlk Evrişim Bloğu
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    
    # İkinci Evrişim Bloğu
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    
    # Üçüncü Evrişim Bloğu
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    
    # Düzleştirme
    tf.keras.layers.Flatten(),
    
    # Tam Bağlantılı Katmanlar
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Model özetini göster
model.summary()

# 3. Modeli Derle
print("\n3. Model Derleniyor...")
print("-" * 30)

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 4. Modeli Eğit
print("\n4. Model Eğitiliyor...")
print("-" * 30)

history = model.fit(
    x_train, y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.2
)

# 5. Modeli Değerlendir
print("\n5. Model Değerlendiriliyor...")
print("-" * 30)

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test doğruluğu: {test_acc:.4f}")

# 6. Eğitim Sürecini Görselleştir
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

# 7. Evrişim Katmanlarını Görselleştir
print("\n7. Evrişim Katmanları Görselleştiriliyor...")
print("-" * 30)

# İlk katmandaki filtreleri görselleştir
ilk_katman_filtreler = model.layers[0].get_weights()[0]
n_filtreler = ilk_katman_filtreler.shape[3]

plt.figure(figsize=(15, 2))
for i in range(n_filtreler):
    plt.subplot(1, n_filtreler, i+1)
    plt.imshow(ilk_katman_filtreler[:, :, 0, i], cmap='viridis')
    plt.axis('off')
    plt.title(f'Filtre {i+1}')

plt.suptitle('İlk Evrişim Katmanındaki Filtreler')
plt.show()

# 8. Örnek Tahminler
print("\n8. Örnek Tahminler Görselleştiriliyor...")
print("-" * 30)

# Rastgele 5 örnek seç
ornek_sayisi = 5
rastgele_indeksler = np.random.randint(0, len(x_test), ornek_sayisi)

plt.figure(figsize=(15, 3))
for i, idx in enumerate(rastgele_indeksler):
    # Tahmin yap
    tahmin = model.predict(x_test[idx:idx+1])
    tahmin_rakam = np.argmax(tahmin)
    
    # Görselleştir
    plt.subplot(1, ornek_sayisi, i+1)
    plt.imshow(x_test[idx].reshape(28, 28), cmap='gray')
    plt.title(f'Tahmin: {tahmin_rakam}\nGerçek: {y_test[idx]}')
    plt.axis('off')

plt.tight_layout()
plt.show() 