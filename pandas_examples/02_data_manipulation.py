"""
Pandas Veri Manipülasyonu
----------------------
Bu örnek, Pandas ile veri manipülasyonu işlemlerini gösterir.
Eksik değerleri ele alma, sütun ekleme/çıkarma ve fonksiyon uygulama gibi konuları içerir.
"""

import pandas as pd
import numpy as np

# Örnek DataFrame oluştur
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, 20, 30, np.nan, 50],
    'C': ['a', 'b', 'c', 'd', np.nan]
})

print("Orijinal DataFrame:")
print(df)

# Eksik değerleri ele alma
print("\nEksik Değerleri Ele Alma:")
print("NA satırlarını sil:")
print(df.dropna())
print("\nNA değerlerini doldur:")
print(df.fillna(0))

# Sütun ekleme/çıkarma
df['D'] = df['A'] * 2
print("\nD sütunu eklendi:")
print(df)

# Sütun silme
df_silinmis = df.drop('B', axis=1)
print("\nB sütunu silindi:")
print(df_silinmis)

# Sıralama
print("\nA sütununa göre sıralanmış:")
print(df.sort_values('A'))

# Fonksiyon uygulama
def deger_ikile(x):
    return x * 2 if pd.notnull(x) else x

print("\nA sütununa özel fonksiyon uygulandı:")
print(df['A'].apply(deger_ikile)) 