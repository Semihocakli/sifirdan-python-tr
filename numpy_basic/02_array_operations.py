# NumPy Dizi Operasyonları
# ======================

"""
NumPy dizileri üzerinde matematiksel işlemler, karşılaştırmalar
ve mantıksal operasyonlar gerçekleştirebiliriz.
"""

import numpy as np

# 1. MATEMATİKSEL OPERASYONLAR
# --------------------------

# Temel diziler
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Temel Matematiksel İşlemler:")
print("Toplama:", a + b)
print("Çıkarma:", b - a)
print("Çarpma:", a * b)
print("Bölme:", b / a)
print("Üs alma:", a ** 2)

# Skaler operasyonlar
print("\nSkaler İşlemler:")
print("Skaler toplama:", a + 2)
print("Skaler çarpma:", a * 3)

# 2. KARŞILAŞTIRMA OPERASYONLARI
# ---------------------------

print("\nKarşılaştırma İşlemleri:")
print("Eşitlik:", a == b)
print("Büyüktür:", a > 2)
print("Küçüktür:", b < 5)
print("Büyük eşittir:", a >= 2)

# 3. MANTIKSAL OPERASYONLAR
# ----------------------

x = np.array([True, False, True])
y = np.array([False, True, True])

print("\nMantıksal İşlemler:")
print("VE (and):", np.logical_and(x, y))
print("VEYA (or):", np.logical_or(x, y))
print("DEĞİL (not):", np.logical_not(x))

# 4. ÖZEL OPERASYONLAR
# -----------------

# Universal fonksiyonlar (ufunc)
arr = np.array([1, 2, 3, 4, 5])
print("\nÖzel Operasyonlar:")
print("Karekök:", np.sqrt(arr))
print("Üstel:", np.exp(arr))
print("Logaritma:", np.log(arr))
print("Sinüs:", np.sin(arr))

# 5. TOPLU İŞLEMLER
# --------------

print("\nToplu İşlemler:")
print("Toplam:", np.sum(arr))
print("Ortalama:", np.mean(arr))
print("Maksimum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standart sapma:", np.std(arr))

# 6. KOŞULLU OPERASYONLAR
# --------------------

# where kullanımı
kosul = arr > 3
print("\nKoşullu İşlemler:")
print("3'ten büyük değerler:", np.where(kosul, arr, 0))

"""
ÖZET
----
1. NumPy dizileri üzerinde vektörel işlemler yapılabilir
2. Matematiksel, mantıksal ve karşılaştırma operatörleri desteklenir
3. Universal fonksiyonlar (ufunc) hızlı işlem yapar
4. Toplu işlemler veri analizi için önemlidir
5. Koşullu operasyonlar veri filtreleme sağlar

İPUÇLARI
-------
1. Vektörel operasyonları döngülere tercih edin
2. Uygun veri tiplerini kullanın
3. Bellek kullanımına dikkat edin
4. Hata kontrolü yapın
5. Performans için optimize edilmiş fonksiyonları kullanın
""" 