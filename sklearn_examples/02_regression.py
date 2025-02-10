"""
Regresyon Analizi (Regression Analysis)
----------------------------------
Bu örnek, scikit-learn ile farklı regresyon modellerinin nasıl uygulanacağını gösterir.

Kullanım Alanları:
- Ev fiyatı tahmini
- Satış tahmini
- Enerji tüketimi tahmini
- Sıcaklık tahmini
- Finansal tahminler

Özellikler:
- Çoklu regresyon modelleri
- Model karşılaştırma
- Performans metrikleri
- Tahmin görselleştirme
- Özellik ölçeklendirme

İşlem Adımları:
1. Veri yükleme: Boston ev fiyatları veri seti
2. Veri hazırlama: Bölme ve ölçeklendirme
3. Model eğitimi: Doğrusal, Ridge ve Lasso regresyon
4. Performans değerlendirme: MSE ve R2 skorları
5. Sonuçların görselleştirilmesi
"""

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

# Veri setini yükle
boston = load_boston()
X, y = boston.data, boston.target  # Özellikler ve hedef değişken

# Veriyi böl ve ölçeklendir
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42  # %20 test verisi
)

scaler = StandardScaler()  # Standartlaştırma için ölçekleyici
X_train_scaled = scaler.fit_transform(X_train)  # Eğitim verisini ölçeklendir
X_test_scaled = scaler.transform(X_test)  # Test verisini ölçeklendir

# Farklı regresyon modellerini karşılaştır
models = {
    'Doğrusal Regresyon': LinearRegression(),
    'Ridge Regresyon': Ridge(alpha=1.0),  # L2 düzenlileştirme
    'Lasso Regresyon': Lasso(alpha=1.0)   # L1 düzenlileştirme
}

results = {}
for name, model in models.items():
    # Modeli eğit
    model.fit(X_train_scaled, y_train)
    
    # Tahmin yap
    y_pred = model.predict(X_test_scaled)
    
    # Metrikleri hesapla
    mse = mean_squared_error(y_test, y_pred)  # Ortalama kare hata
    r2 = r2_score(y_test, y_pred)  # R-kare skoru
    
    results[name] = {'MSE': mse, 'R2': r2}
    print(f"\n{name}:")
    print(f"Ortalama Kare Hata: {mse:.2f}")
    print(f"R-kare Skoru: {r2:.2f}")

# Tahmin vs gerçek değerleri görselleştir
plt.figure(figsize=(15, 5))
for i, (name, model) in enumerate(models.items(), 1):
    plt.subplot(1, 3, i)
    y_pred = model.predict(X_test_scaled)
    plt.scatter(y_test, y_pred, alpha=0.5)  # Saçılım grafiği
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # İdeal çizgi
    plt.xlabel('Gerçek Değerler')
    plt.ylabel('Tahmin Edilen Değerler')
    plt.title(f'{name}\nR² = {results[name]["R2"]:.2f}')

plt.tight_layout()  # Alt grafikler arası boşlukları otomatik ayarlama
plt.show()  # Grafiği göster 