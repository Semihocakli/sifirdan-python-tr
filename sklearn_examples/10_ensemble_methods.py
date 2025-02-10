"""
Topluluk Öğrenme Yöntemleri (Ensemble Methods)
----------------------------------------
Bu örnek, scikit-learn ile topluluk öğrenme yöntemlerini gösterir.
Kullanım Alanları: Sınıflandırma, Regresyon, Tahmin problemleri
Özellikler: Rastgele Orman, Gradyan Artırma, AdaBoost, Oylama/Yığınlama
"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier,
    VotingClassifier
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Örnek veri seti oluştur
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    random_state=42
)

# Veriyi eğitim ve test setlerine böl
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Veriyi ölçeklendir
olcekleyici = StandardScaler()
X_train_scaled = olcekleyici.fit_transform(X_train)
X_test_scaled = olcekleyici.transform(X_test)

# Temel modelleri tanımla
rf = RandomForestClassifier(n_estimators=100, random_state=42)
gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
ada = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1),
    n_estimators=100,
    random_state=42
)

# Oylama sınıflandırıcısını oluştur
voting_clf = VotingClassifier(
    estimators=[
        ('rf', rf),
        ('gb', gb),
        ('ada', ada)
    ],
    voting='soft'
)

# Modelleri eğit ve değerlendir
modeller = {
    'Rastgele Orman': rf,
    'Gradyan Artırma': gb,
    'AdaBoost': ada,
    'Oylama': voting_clf
}

sonuclar = {}
for isim, model in modeller.items():
    # Modeli eğit
    model.fit(X_train_scaled, y_train)
    
    # Tahminler yap
    y_pred = model.predict(X_test_scaled)
    
    # Performansı değerlendir
    dogruluk = accuracy_score(y_test, y_pred)
    sonuclar[isim] = dogruluk
    
    print(f"\n{isim} Sonuçları:")
    print("-" * 50)
    print(f"Doğruluk: {dogruluk:.4f}")
    print("\nSınıflandırma Raporu:")
    print(classification_report(y_test, y_pred))

# Sonuçları görselleştir
plt.figure(figsize=(10, 6))
plt.bar(sonuclar.keys(), sonuclar.values())
plt.title('Model Karşılaştırması')
plt.xlabel('Model')
plt.ylabel('Doğruluk Skoru')
plt.ylim(0.8, 1.0)  # Daha iyi görselleştirme için y eksenini ayarla
plt.xticks(rotation=45)
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()

# Özellik önemlerini görselleştir (Rastgele Orman için)
ozellik_onemler = pd.DataFrame({
    'ozellik': [f'Özellik_{i}' for i in range(X.shape[1])],
    'onem': rf.feature_importances_
}).sort_values('onem', ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(ozellik_onemler['ozellik'], ozellik_onemler['onem'])
plt.title('Rastgele Orman - Özellik Önemleri')
plt.xlabel('Özellik')
plt.ylabel('Önem Skoru')
plt.xticks(rotation=45)
plt.grid(True, axis='y')
plt.tight_layout()
plt.show() 