"""
TensorFlow Model Kaydetme ve Yükleme
--------------------------------
Eğitilmiş modelleri kaydetme ve daha sonra kullanma yöntemlerini gösterir.
Bu özellik, uzun süren eğitimlerin sonuçlarını saklamak için önemlidir.

Özellikler:
- Model kaydetme formatları
- Ağırlık kaydetme
- Model yükleme
- SavedModel formatı
"""

import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt

# 1. Basit Bir Model Oluştur
print("1. Model Oluşturuluyor...")
print("-" * 30)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Model yapısını göster
model.summary()

# 2. Örnek Veri Oluştur ve Modeli Eğit
print("\n2. Model Eğitiliyor...")
print("-" * 30)

# Rastgele veri oluştur
X = np.random.random((1000, 10))
y = np.random.randint(2, size=(1000, 1))

# Modeli eğit
history = model.fit(X, y, epochs=5, validation_split=0.2)

# 3. Modeli Farklı Formatlarda Kaydet
print("\n3. Model Kaydediliyor...")
print("-" * 30)

# Klasör oluştur
if not os.path.exists('kaydedilen_modeller'):
    os.makedirs('kaydedilen_modeller')

# 3.1. Tüm modeli HDF5 formatında kaydet
model.save('kaydedilen_modeller/tam_model.h5')
print("Tüm model HDF5 formatında kaydedildi.")

# 3.2. Sadece ağırlıkları kaydet
model.save_weights('kaydedilen_modeller/model_agirliklari')
print("Model ağırlıkları kaydedildi.")

# 3.3. SavedModel formatında kaydet
model.save('kaydedilen_modeller/saved_model')
print("Model SavedModel formatında kaydedildi.")

# 4. Kaydedilen Modelleri Yükle
print("\n4. Kaydedilen Modeller Yükleniyor...")
print("-" * 30)

# 4.1. HDF5 modelini yükle
model_h5 = tf.keras.models.load_model('kaydedilen_modeller/tam_model.h5')
print("HDF5 model yüklendi.")

# 4.2. Yeni model oluştur ve ağırlıkları yükle
yeni_model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
yeni_model.load_weights('kaydedilen_modeller/model_agirliklari')
print("Model ağırlıkları yüklendi.")

# 4.3. SavedModel'i yükle
model_saved = tf.keras.models.load_model('kaydedilen_modeller/saved_model')
print("SavedModel yüklendi.")

# 5. Modelleri Karşılaştır
print("\n5. Model Karşılaştırması Yapılıyor...")
print("-" * 30)

# Test verisi oluştur
X_test = np.random.random((100, 10))
y_test = np.random.randint(2, size=(100, 1))

# Her modeli değerlendir
sonuclar = {
    'Orijinal Model': model.evaluate(X_test, y_test),
    'HDF5 Model': model_h5.evaluate(X_test, y_test),
    'Ağırlık Yüklenmiş Model': yeni_model.evaluate(X_test, y_test),
    'SavedModel': model_saved.evaluate(X_test, y_test)
}

for model_adi, (kayip, dogruluk) in sonuclar.items():
    print(f"\n{model_adi}:")
    print(f"Kayıp: {kayip:.4f}")
    print(f"Doğruluk: {dogruluk:.4f}")

# 6. Tahmin Karşılaştırması
print("\n6. Tahmin Karşılaştırması...")
print("-" * 30)

# Örnek veri
ornek_veri = np.random.random((1, 10))

tahminler = {
    'Orijinal Model': model.predict(ornek_veri)[0][0],
    'HDF5 Model': model_h5.predict(ornek_veri)[0][0],
    'Ağırlık Yüklenmiş Model': yeni_model.predict(ornek_veri)[0][0],
    'SavedModel': model_saved.predict(ornek_veri)[0][0]
}

for model_adi, tahmin in tahminler.items():
    print(f"{model_adi} tahmini: {tahmin:.4f}")

# 7. Model Bilgilerini Görüntüle
print("\n7. Model Bilgileri...")
print("-" * 30)

# Model konfigürasyonunu göster
config = model.get_config()
print("\nModel Konfigürasyonu:")
print("-" * 20)
for layer in config['layers']:
    print(f"Katman: {layer['class_name']}")
    print(f"Konfigürasyon: {layer['config']}\n") 