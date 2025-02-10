"""
Temel Sınıflandırma (Basic Classification)
-------------------------------------
Bu örnek, scikit-learn ile temel sınıflandırma işlemlerinin nasıl yapılacağını gösterir.

Kullanım Alanları:
- Görüntü sınıflandırma
- Metin kategorizasyonu
- Müşteri segmentasyonu
- Hastalık teşhisi
- Spam tespiti

Özellikler:
- Veri ön işleme
- Model eğitimi
- Performans değerlendirme
- Görselleştirme
- Çok sınıflı sınıflandırma

İşlem Adımları:
1. Veri yükleme: Iris veri seti
2. Veri bölme: Eğitim ve test setleri
3. Özellik ölçeklendirme: StandardScaler
4. Model eğitimi: Lojistik Regresyon
5. Performans değerlendirme: Sınıflandırma raporu ve karmaşıklık matrisi
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükle
iris = load_iris()
X, y = iris.data, iris.target  # Özellikler ve hedef değişken

# Veriyi eğitim ve test olarak böl
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42  # %20 test verisi
)

# Özellikleri ölçeklendir
scaler = StandardScaler()  # Standartlaştırma için ölçekleyici
X_train_scaled = scaler.fit_transform(X_train)  # Eğitim verisini ölçeklendir
X_test_scaled = scaler.transform(X_test)  # Test verisini ölçeklendir

# Modeli eğit
model = LogisticRegression(multi_class='multinomial')  # Çok sınıflı lojistik regresyon
model.fit(X_train_scaled, y_train)  # Modeli eğit

# Tahmin yap
y_pred = model.predict(X_test_scaled)  # Test verisi üzerinde tahmin yap

# Sonuçları yazdır
print("Sınıflandırma Raporu:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Karmaşıklık matrisini çiz
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred)  # Karmaşıklık matrisi hesapla
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.title('Karmaşıklık Matrisi')
plt.ylabel('Gerçek Etiket')
plt.xlabel('Tahmin Edilen Etiket')
plt.show() 