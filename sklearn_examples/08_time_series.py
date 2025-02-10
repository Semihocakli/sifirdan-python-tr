"""
Zaman Serisi Analizi (Time Series Analysis)
------------------------------------
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns

# Örnek zaman serisi verisi oluştur
np.random.seed(42)
tarihler = pd.date_range(start='2020-01-01', end='2023-12-31', freq='D')
n_samples = len(tarihler)

# Trend, mevsimsellik ve gürültü içeren zaman serisi oluştur
trend = np.linspace(0, 100, n_samples)
mevsimsellik = 10 * np.sin(2 * np.pi * np.arange(n_samples) / 365)
gurultu = np.random.normal(0, 5, n_samples)
degerler = trend + mevsimsellik + gurultu

df = pd.DataFrame({
    'tarih': tarihler,
    'deger': degerler
})

# Zaman serisi için özellik mühendisliği
def ozellik_olustur(df):
    df = df.copy()
    df['yil'] = df['tarih'].dt.year
    df['ay'] = df['tarih'].dt.month
    df['gun'] = df['tarih'].dt.day
    df['haftanin_gunu'] = df['tarih'].dt.dayofweek
    df['ceyrek'] = df['tarih'].dt.quarter
    
    # Gecikme özellikleri
    df['gecikme_1'] = df['deger'].shift(1)
    df['gecikme_7'] = df['deger'].shift(7)
    df['gecikme_30'] = df['deger'].shift(30)
    
    # Hareketli ortalama özellikleri
    df['hareketli_ort_7'] = df['deger'].rolling(window=7).mean()
    df['hareketli_std_7'] = df['deger'].rolling(window=7).std()
    
    return df

# Özellikleri oluştur
df_ozellikler = ozellik_olustur(df)
df_ozellikler = df_ozellikler.dropna()

# Modelleme için veriyi hazırla
X = df_ozellikler.drop(['tarih', 'deger'], axis=1)
y = df_ozellikler['deger']

# Zaman serisi çapraz doğrulama
tscv = TimeSeriesSplit(n_splits=5)

# Modelleri karşılaştır
modeller = {
    'Doğrusal Regresyon': LinearRegression(),
    'Rastgele Orman': RandomForestRegressor(n_estimators=100, random_state=42)
}

sonuclar = {}
for isim, model in modeller.items():
    mse_skorlari = []
    
    for train_idx, test_idx in tscv.split(X):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
        
        # Özellikleri ölçekle
        olcekleyici = StandardScaler()
        X_train_scaled = olcekleyici.fit_transform(X_train)
        X_test_scaled = olcekleyici.transform(X_test)
        
        # Eğit ve tahmin et
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        mse = mean_squared_error(y_test, y_pred)
        mse_skorlari.append(mse)
    
    sonuclar[isim] = mse_skorlari
    print(f"{isim} - Ortalama MSE: {np.mean(mse_skorlari):.2f}")

# Sonuçları görselleştir
plt.figure(figsize=(15, 5))

# Orijinal zaman serisi
plt.subplot(131)
plt.plot(df['tarih'], df['deger'])
plt.title('Orijinal Zaman Serisi')
plt.xticks(rotation=45)

# Özellik önemleri (Rastgele Orman için)
plt.subplot(132)
rf_model = modeller['Rastgele Orman']
onemler = pd.DataFrame({
    'ozellik': X.columns,
    'onem': rf_model.feature_importances_
}).sort_values('onem', ascending=False)

sns.barplot(data=onemler, x='onem', y='ozellik')
plt.title('Özellik Önemleri')

# Çapraz doğrulama sonuçları
plt.subplot(133)
plt.boxplot([sonuclar[isim] for isim in modeller.keys()], labels=modeller.keys())
plt.title('Model Karşılaştırması')
plt.ylabel('MSE')

plt.tight_layout()
plt.show() 