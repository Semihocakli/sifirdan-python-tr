"""
Özellik Mühendisliği (Feature Engineering)
-------------------------------------
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükle
data = load_breast_cancer()
X, y = data.data, data.target

# Veriyi böl
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Polinom Özellikleri
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X_train)
print(f"Orijinal özellikler: {X_train.shape[1]}")
print(f"Polinom özellikleri: {X_poly.shape[1]}")

# 2. SelectKBest ile Özellik Seçimi
selector = SelectKBest(score_func=f_classif, k=10)
X_selected = selector.fit_transform(X_train, y_train)
selected_features_mask = selector.get_support()

# Özellik skorlarını çiz
plt.figure(figsize=(12, 5))
plt.bar(range(X_train.shape[1]), selector.scores_)
plt.xlabel('Özellik İndeksi')
plt.ylabel('F-skoru')
plt.title('Özellik Önem Skorları')
plt.show()

# 3. Özyinelemeli Özellik Eleme (RFE)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rfe = RFE(estimator=rf, n_features_to_select=10)
X_rfe = rfe.fit_transform(X_train, y_train)

# RFE seçili özelliklerini çiz
plt.figure(figsize=(12, 5))
plt.bar(range(X_train.shape[1]), rfe.ranking_)
plt.xlabel('Özellik İndeksi')
plt.ylabel('Sıralama')
plt.title('RFE Özellik Sıralamaları')
plt.show()

# 4. Rastgele Orman Özellik Önemleri
rf.fit(X_train, y_train)
importances = rf.feature_importances_

# Özellik önemlerini çiz
plt.figure(figsize=(12, 5))
plt.bar(range(X_train.shape[1]), importances)
plt.xlabel('Özellik İndeksi')
plt.ylabel('Önem')
plt.title('Rastgele Orman Özellik Önemleri')
plt.show()

# Farklı özellik seçim yöntemlerinin performansını karşılaştır
results = {}
for name, X_features in [
    ('Orijinal', X_train),
    ('Polinom', X_poly),
    ('SelectKBest', X_selected),
    ('RFE', X_rfe)
]:
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_features, y_train)
    score = rf.score(X_test, y_test)
    results[name] = score
    print(f"{name} özellikleri doğruluğu: {score:.4f}") 