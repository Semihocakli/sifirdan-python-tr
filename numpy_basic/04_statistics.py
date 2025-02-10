# NumPy İstatistiksel İşlemler
# =========================

"""
NumPy, veri analizi için güçlü istatistiksel fonksiyonlar sunar.
Bu fonksiyonlar büyük veri setlerinde hızlı hesaplamalar yapar.
"""

import numpy as np

# 1. TEMEL İSTATİSTİKLER
# --------------------

# Örnek veri seti
veri = np.array([14, 25, 14, 18, 21, 25, 29, 23, 27, 16, 
                 18, 20, 22, 24, 26, 28, 30, 32, 24, 26])
print("Veri seti:", veri)

# Merkezi eğilim ölçüleri
print("\nMerkezi Eğilim Ölçüleri:")
print("Ortalama:", np.mean(veri))
print("Medyan:", np.median(veri))
print("Mod:", np.bincount(veri).argmax())  # En sık tekrar eden değer

# Dağılım ölçüleri
print("\nDağılım Ölçüleri:")
print("Standart sapma:", np.std(veri))
print("Varyans:", np.var(veri))
print("Minimum:", np.min(veri))
print("Maksimum:", np.max(veri))
print("Aralık:", np.ptp(veri))  # Peak to peak (max - min)

# 2. YÜZDELIK VE ÇEYREKLER
# ----------------------

print("\nYüzdelik ve Çeyrekler:")
print("25. yüzdelik (Q1):", np.percentile(veri, 25))
print("50. yüzdelik (Q2/Medyan):", np.percentile(veri, 50))
print("75. yüzdelik (Q3):", np.percentile(veri, 75))
print("Çeyrekler arası aralık (IQR):", 
      np.percentile(veri, 75) - np.percentile(veri, 25))

# 3. KORELASYON VE KOVARYANS
# ------------------------

# İki değişken arasındaki ilişki
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

print("\nKorelasyon ve Kovaryans:")
print("Korelasyon katsayısı:", np.corrcoef(x, y)[0, 1])
print("Kovaryans:", np.cov(x, y)[0, 1])

# 4. FREKANS ANALİZİ
# ----------------

# Benzersiz değerler ve frekansları
benzersiz, frekanslar = np.unique(veri, return_counts=True)
print("\nFrekans Analizi:")
for deger, frekans in zip(benzersiz, frekanslar):
    print(f"{deger}: {frekans} kez")

# 5. SIRALI İSTATİSTİKLER
# ---------------------

print("\nSıralı İstatistikler:")
sirali = np.sort(veri)
print("Sıralı veri:", sirali)
print("En küçük 3 değer:", sirali[:3])
print("En büyük 3 değer:", sirali[-3:])

# 6. ÇAPRAZ TABLO (CONTINGENCY TABLE)
# -------------------------------

# İki kategorik değişken arasındaki ilişki
kategori1 = np.array(['A', 'A', 'B', 'B', 'A', 'B'])
kategori2 = np.array(['X', 'Y', 'X', 'Y', 'X', 'Y'])

# Çapraz tablo oluşturma
capraz_tablo = np.unique(kategori1, return_counts=True)[1]
print("\nÇapraz Tablo:")
print(capraz_tablo)

"""
ÖZET
----
1. NumPy temel istatistiksel hesaplamalar için fonksiyonlar sunar
2. Merkezi eğilim ve dağılım ölçüleri hesaplanabilir
3. Yüzdelik ve çeyrek değerler analiz edilebilir
4. Korelasyon ve kovaryans hesaplanabilir
5. Frekans analizi yapılabilir

İPUÇLARI
-------
1. Büyük veri setlerinde np.nanmean() gibi NaN'ları yok sayan fonksiyonları kullanın
2. Veri tipine uygun istatistiksel fonksiyonu seçin
3. Çok boyutlu dizilerde axis parametresini doğru kullanın
4. Aykırı değerlere dikkat edin
5. İstatistiksel varsayımları kontrol edin
""" 