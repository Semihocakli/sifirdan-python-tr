"""
Anomali Tespiti (Anomaly Detection)
--------------------------------
Bu örnek, scikit-learn ile anomali tespiti yöntemlerini gösterir.
Kullanım Alanları: Dolandırıcılık tespiti, Sistem arızalarının tespiti, Kalite kontrol
Özellikler: İzolasyon Ormanı, Yerel Aykırı Faktör (LOF), Tek Sınıflı SVM
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt

# Örnek veri oluştur
np.random.seed(42)
n_samples = 300
n_outliers = 15

# Normal veriler
normal_data = np.random.randn(n_samples - n_outliers, 2)

# Aykırı değerler
outlier_data = np.random.uniform(low=-4, high=4, size=(n_outliers, 2))

# Verileri birleştir
X = np.vstack([normal_data, outlier_data])

# Veriyi ölçeklendir
olcekleyici = StandardScaler()
X_scaled = olcekleyici.fit_transform(X)

# Anomali tespit modellerini tanımla
modeller = {
    'İzolasyon Ormanı': IsolationForest(contamination=0.05, random_state=42),
    'Yerel Aykırı Faktör': LocalOutlierFactor(n_neighbors=20, contamination=0.05),
    'Tek Sınıflı SVM': OneClassSVM(kernel='rbf', nu=0.05)
}

# Her model için anomali tespiti yap ve görselleştir
plt.figure(figsize=(15, 5))

for idx, (isim, model) in enumerate(modeller.items(), 1):
    plt.subplot(1, 3, idx)
    
    if isinstance(model, LocalOutlierFactor):
        y_pred = model.fit_predict(X_scaled)
    else:
        y_pred = model.fit(X_scaled).predict(X_scaled)
    
    # Anomali etiketlerini -1'den 0'a dönüştür
    y_pred = np.where(y_pred == -1, 0, 1)
    
    # Sonuçları görselleştir
    plt.scatter(X_scaled[y_pred == 1, 0], X_scaled[y_pred == 1, 1],
               c='blue', label='Normal')
    plt.scatter(X_scaled[y_pred == 0, 0], X_scaled[y_pred == 0, 1],
               c='red', label='Anomali')
    
    plt.title(f'{isim}\nTespit Edilen Anomali Sayısı: {np.sum(y_pred == 0)}')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()

# Model performanslarını karşılaştır
print("\nModel Performansları:")
print("-" * 50)

for isim, model in modeller.items():
    if isinstance(model, LocalOutlierFactor):
        y_pred = model.fit_predict(X_scaled)
    else:
        y_pred = model.fit(X_scaled).predict(X_scaled)
    
    anomali_sayisi = np.sum(y_pred == -1)
    anomali_orani = anomali_sayisi / len(X) * 100
    
    print(f"{isim}:")
    print(f"Tespit Edilen Anomali Sayısı: {anomali_sayisi}")
    print(f"Anomali Oranı: {anomali_orani:.2f}%")
    print("-" * 50) 