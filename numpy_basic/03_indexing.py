# NumPy Dizilerinde İndeksleme ve Dilimleme
# =====================================

"""
NumPy dizilerinde indeksleme ve dilimleme işlemleri,
dizinin belirli elemanlarına veya alt kümelerine erişmemizi sağlar.
"""

import numpy as np

# 1. TEK BOYUTLU DİZİLERDE İNDEKSLEME
# ---------------------------------

# Örnek dizi
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print("Orijinal dizi:", arr)

# Tek eleman erişimi
print("\nTek Eleman Erişimi:")
print("İlk eleman:", arr[0])
print("Son eleman:", arr[-1])
print("Üçüncü eleman:", arr[2])

# 2. DİLİMLEME (SLICING)
# --------------------

print("\nDilimleme Örnekleri:")
print("İlk üç eleman:", arr[:3])
print("Son üç eleman:", arr[-3:])
print("Ortadaki elemanlar:", arr[3:6])
print("İkişer atlayarak:", arr[::2])
print("Tersten:", arr[::-1])

# 3. ÇOK BOYUTLU DİZİLERDE İNDEKSLEME
# --------------------------------

# 2x3 matris
matris = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("\nMatris:\n", matris)

# Eleman erişimi
print("\nMatris Eleman Erişimi:")
print("İlk satır, ikinci sütun:", matris[0, 1])
print("Son satır, son sütun:", matris[-1, -1])

# 4. ÇOK BOYUTLU DİLİMLEME
# ----------------------

print("\nMatris Dilimleme:")
print("İlk satır:", matris[0, :])
print("Son sütun:", matris[:, -1])
print("Alt matris:\n", matris[0:2, 1:3])

# 5. BOOLEAN İNDEKSLEME
# ------------------

# Koşula göre eleman seçme
kosul = arr > 50
print("\nBoolean İndeksleme:")
print("50'den büyük elemanlar:", arr[kosul])

# Çoklu koşul
kosul2 = (arr > 30) & (arr < 70)
print("30 ile 70 arası elemanlar:", arr[kosul2])

# 6. FANCY İNDEKSLEME
# ----------------

# İndeks dizisi ile seçim
indeksler = [1, 3, 5]
print("\nFancy İndeksleme:")
print("Seçili indekslerdeki elemanlar:", arr[indeksler])

# 7. İNDEKSLEME İLE DEĞİŞİKLİK
# -------------------------

# Tek eleman değiştirme
kopya = arr.copy()
kopya[0] = 100
print("\nDeğişiklik Örnekleri:")
print("Orijinal dizi:", arr)
print("Değiştirilmiş kopya:", kopya)

# Dilim değiştirme
kopya[1:4] = 200
print("Dilim değiştirilmiş:", kopya)

"""
ÖZET
----
1. İndeksleme tek eleman erişimi sağlar
2. Dilimleme alt kümelere erişim sağlar
3. Çok boyutlu dizilerde virgülle ayrılmış indeksler kullanılır
4. Boolean indeksleme koşullu seçim yapar
5. Fancy indeksleme indeks dizisiyle seçim yapar

İPUÇLARI
-------
1. Negatif indeksleri dikkatli kullanın
2. View ve copy farkına dikkat edin
3. İndeks sınırlarını kontrol edin
4. Boolean maskeleri optimize edin
5. Gereksiz kopyalamadan kaçının
""" 