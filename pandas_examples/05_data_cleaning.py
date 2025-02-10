"""
Pandas Veri Temizleme
-------------------
Bu örnek, Pandas ile veri temizleme ve ön işleme adımlarını gösterir.
Eksik değerleri ele alma, aykırı değerleri tespit etme ve veri dönüşümü gibi konuları içerir.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Türkçe karakter desteği için
plt.rcParams['font.family'] = 'DejaVu Sans'

# Kirli veri seti oluştur
np.random.seed(42)
veri = pd.DataFrame({
    'yas': np.random.randint(18, 80, 100),
    'gelir': np.random.normal(5000, 2000, 100),
    'egitim_yili': np.random.randint(8, 20, 100),
    'sehir': np.random.choice(['İstanbul', 'Ankara', 'İzmir', None], 100)
})

# Bazı değerleri NA yap
veri.loc[np.random.choice(veri.index, 10), 'yas'] = np.nan
veri.loc[np.random.choice(veri.index, 10), 'gelir'] = np.nan
veri.loc[np.random.choice(veri.index, 10), 'egitim_yili'] = np.nan

print("Orijinal Veri:")
print(veri.head())
print("\nEksik Değer Özeti:")
print(veri.isnull().sum())

# Eksik değerleri doldur
veri['yas'] = veri['yas'].fillna(veri['yas'].mean())
veri['gelir'] = veri['gelir'].fillna(veri['gelir'].median())
veri['egitim_yili'] = veri['egitim_yili'].fillna(veri['egitim_yili'].mode()[0])
veri['sehir'] = veri['sehir'].fillna('Bilinmiyor')

print("\nEksik Değerler Doldurulduktan Sonra:")
print(veri.isnull().sum())

# Aykırı değerleri tespit et (Z-score yöntemi)
def aykiri_deger_bul(seri, esik=3):
    z_score = np.abs((seri - seri.mean()) / seri.std())
    return z_score > esik

# Gelir için aykırı değerleri göster
aykirilar = aykiri_deger_bul(veri['gelir'])
print(f"\nGelir'de Aykırı Değer Sayısı: {aykirilar.sum()}")
print("Aykırı Gelir Değerleri:")
print(veri[aykirilar]['gelir'])

# Veri dönüşümü
# Gelir değerlerini log ölçeğine dönüştür
veri['log_gelir'] = np.log1p(veri['gelir'])

# Kategorik değişkeni sayısallaştır
veri = pd.get_dummies(veri, columns=['sehir'], prefix='sehir')

print("\nDönüştürülmüş Veri:")
print(veri.head())

# Görselleştirme
plt.figure(figsize=(12, 4))

# Orijinal gelir dağılımı
plt.subplot(121)
plt.hist(veri['gelir'], bins=30)
plt.title('Orijinal Gelir Dağılımı')
plt.xlabel('Gelir')
plt.ylabel('Frekans')

# Log dönüşümlü gelir dağılımı
plt.subplot(122)
plt.hist(veri['log_gelir'], bins=30)
plt.title('Log Dönüşümlü Gelir Dağılımı')
plt.xlabel('Log Gelir')
plt.ylabel('Frekans')

plt.tight_layout()
plt.show()

# Korelasyon analizi
korelasyon = veri[['yas', 'gelir', 'egitim_yili', 'log_gelir']].corr()
print("\nKorelasyon Matrisi:")
print(korelasyon.round(2)) 