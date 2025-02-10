"""
Pandas Veri Analizi
-----------------
Bu örnek, Pandas ile temel veri analizi işlemlerini gösterir.
Gruplama, birleştirme ve istatistiksel hesaplamalar gibi konuları içerir.
"""

import pandas as pd
import numpy as np

# Örnek veri setleri oluştur
satis_verileri = pd.DataFrame({
    'tarih': pd.date_range('2023-01-01', periods=6),
    'magaza': ['A', 'B', 'A', 'B', 'A', 'B'],
    'urun': ['Elma', 'Muz', 'Elma', 'Muz', 'Portakal', 'Portakal'],
    'miktar': [10, 15, 12, 18, 8, 20],
    'fiyat': [2.5, 3.0, 2.5, 3.0, 4.0, 4.0]
})

magaza_bilgileri = pd.DataFrame({
    'magaza': ['A', 'B'],
    'sehir': ['İstanbul', 'Ankara'],
    'calisan_sayisi': [5, 7]
})

print("Satış Verileri:")
print(satis_verileri)
print("\nMağaza Bilgileri:")
print(magaza_bilgileri)

# Gruplama ve toplama
print("\nMağaza bazında toplam satış:")
print(satis_verileri.groupby('magaza')['miktar'].sum())

# Birleştirme işlemi
birlesik_veri = pd.merge(satis_verileri, magaza_bilgileri, on='magaza')
print("\nBirleştirilmiş Veri:")
print(birlesik_veri)

# İstatistiksel analiz
print("\nÜrün bazında istatistikler:")
print(satis_verileri.groupby('urun').agg({
    'miktar': ['mean', 'sum', 'count'],
    'fiyat': ['mean', 'min', 'max']
}).round(2))

# Pivot tablo
pivot_tablo = pd.pivot_table(satis_verileri, 
                           values='miktar',
                           index='magaza',
                           columns='urun',
                           aggfunc='sum',
                           fill_value=0)
print("\nPivot Tablo (Mağaza-Ürün Bazında Miktar):")
print(pivot_tablo) 