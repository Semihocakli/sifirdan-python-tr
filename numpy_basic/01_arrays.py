# NumPy Dizileri (Arrays)
# ====================

"""
NumPy, bilimsel hesaplamalar için Python'ın temel kütüphanesidir.
ndarray (n-dimensional array) sınıfı, aynı türde verileri tutan çok boyutlu bir dizidir.
"""

import numpy as np

# 1. DİZİ OLUŞTURMA YÖNTEMLERİ
# --------------------------

# Liste kullanarak dizi oluşturma
liste = [1, 2, 3, 4, 5]
arr1 = np.array(liste)
print("1. Liste kullanarak:", arr1)

# Doğrudan dizi oluşturma
arr2 = np.array([1, 2, 3, 4, 5])
print("2. Doğrudan:", arr2)

# Sıfırlardan oluşan dizi
zeros = np.zeros(5)
print("3. Sıfırlar:", zeros)

# Birlerden oluşan dizi
ones = np.ones(5)
print("4. Birler:", ones)

# Belirli aralıkta dizi
aralik = np.arange(0, 10, 2)  # 0'dan 10'a kadar 2'şer artarak
print("5. Aralık:", aralik)

# Eşit aralıklı sayılar
esit_aralik = np.linspace(0, 1, 5)  # 0 ile 1 arasında 5 eşit aralıklı sayı
print("6. Eşit aralık:", esit_aralik)

# 2. ÇOK BOYUTLU DİZİLER
# --------------------

# 2x3 boyutunda dizi
matris = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("\nMatris:\n", matris)

# 3x3 sıfır matrisi
sifir_matris = np.zeros((3, 3))
print("\nSıfır matrisi:\n", sifir_matris)

# 3. DİZİ ÖZELLİKLERİ
# -----------------

print("\nDizi Özellikleri:")
print("Boyut sayısı:", matris.ndim)  # Kaç boyutlu?
print("Şekil:", matris.shape)        # Her boyuttaki eleman sayısı
print("Eleman sayısı:", matris.size) # Toplam eleman sayısı
print("Veri tipi:", matris.dtype)    # Elemanların veri tipi

# 4. VERİ TİPLERİ
# -------------

# Tam sayı dizisi
int_arr = np.array([1, 2, 3], dtype=np.int32)
print("\nTam sayı dizisi:", int_arr)

# Ondalıklı sayı dizisi
float_arr = np.array([1, 2, 3], dtype=np.float64)
print("Ondalıklı sayı dizisi:", float_arr)

# Veri tipi dönüşümü
donusum = int_arr.astype(np.float64)
print("Dönüştürülmüş dizi:", donusum)

"""
ÖZET
----
1. NumPy dizileri, aynı türde verileri tutan çok boyutlu yapılardır
2. Farklı yöntemlerle dizi oluşturulabilir (liste, arange, zeros, ones vb.)
3. Çok boyutlu diziler matris ve tensör işlemleri için uygundur
4. Dizilerin boyut, şekil, eleman sayısı gibi özellikleri vardır
5. Farklı veri tipleri desteklenir ve dönüşümler yapılabilir

İPUÇLARI
-------
1. Büyük veriler için uygun veri tipi seçin
2. Bellek kullanımına dikkat edin
3. Vektörleştirilmiş operasyonları tercih edin
4. Dizi özelliklerini kontrol edin
5. Veri tipi dönüşümlerinde dikkatli olun
""" 