"""
Pandas Temel İşlemler
------------------
Bu örnek, Pandas kütüphanesinin temel işlemlerini gösterir.
DataFrame oluşturma, veri erişimi ve filtreleme gibi temel konuları içerir.
"""

import pandas as pd
import numpy as np

# DataFrame Oluşturma
print("DataFrame Oluşturma:")

# Sözlükten oluşturma
veri_sozluk = {
    'isim': ['Ahmet', 'Ayşe', 'Mehmet', 'Zeynep'],
    'yas': [28, 22, 35, 32],
    'sehir': ['İstanbul', 'Ankara', 'İzmir', 'Bursa']
}
df1 = pd.DataFrame(veri_sozluk)
print("\nSözlükten:")
print(df1)

# Liste listesinden oluşturma
veri_liste = [
    ['Ahmet', 28, 'İstanbul'],
    ['Ayşe', 22, 'Ankara'],
    ['Mehmet', 35, 'İzmir']
]
df2 = pd.DataFrame(veri_liste, columns=['isim', 'yas', 'sehir'])
print("\nListeden:")
print(df2)

# Temel işlemler
print("\nTemel İşlemler:")
print("DataFrame'in İlk Satırları:", df1.head(2))
print("\nDataFrame Bilgisi:")
print(df1.info())
print("\nDataFrame İstatistikleri:")
print(df1.describe())

# Veriye erişim
print("\nVeriye Erişim:")
print("Tek sütun:", df1['isim'])
print("\nBirden fazla sütun:")
print(df1[['isim', 'yas']])

# Temel filtreleme
print("\nFiltreleme:")
print("Yaş > 30:")
print(df1[df1['yas'] > 30]) 