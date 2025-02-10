# NumPy Gelişmiş İndeksleme
# ========================

"""
NumPy'da gelişmiş indeksleme yöntemleri, karmaşık seçim işlemlerini
kolayca yapmamızı sağlar. Boolean indeksleme, fancy indeksleme ve
bunların kombinasyonları kullanılabilir.
"""

import numpy as np

# 1. BOOLEAN İNDEKSLEME
# ------------------

# Örnek dizi
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Orijinal dizi:", arr)

# Koşullu seçim
kosul = arr > 5
print("\nKoşul maski:", kosul)
print("5'ten büyük elemanlar:", arr[kosul])

# Çoklu koşul
kosul2 = (arr > 3) & (arr < 7)
print("3 ile 7 arasındaki elemanlar:", arr[kosul2])

# 2. FANCY İNDEKSLEME
# ----------------

# İndeks dizisi ile seçim
indeksler = [0, 2, 4]  # İstenen indeksler
print("\nFancy indeksleme:")
print("Seçili indekslerdeki elemanlar:", arr[indeksler])

# Çok boyutlu dizilerde fancy indeksleme
matris = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\nMatris:\n", matris)

satir_ind = [0, 2]
sutun_ind = [1, 2]
print("Seçili elemanlar:", matris[satir_ind, sutun_ind])

# 3. BOOLEAN VE FANCY İNDEKSLEME KARIŞIMI
# -----------------------------------

# Örnek: Belirli indekslerdeki pozitif sayıları seç
arr = np.array([1, -2, 3, -4, 5, -6, 7, -8, 9])
indeksler = [0, 2, 4, 6, 8]
kosul = arr > 0

print("\nKarışık indeksleme:")
print("Seçili pozitif sayılar:", arr[indeksler][arr[indeksler] > 0])

# 4. GELİŞMİŞ DİLİMLEME
# -------------------

# Adımlı dilimleme
arr = np.arange(10)
print("\nGelişmiş dilimleme:")
print("Her ikinci eleman:", arr[::2])
print("Tersten her üçüncü eleman:", arr[::-3])

# 5. İNDEKS MASKELEME
# ----------------

# Maske oluşturma
maske = np.array([True, False, True, False, True])
veri = np.array([1, 2, 3, 4, 5])
print("\nMaske ile seçim:", veri[maske])

# 6. KOŞULLU DEĞİŞTİRME
# -------------------

# where kullanımı
arr = np.array([1, 2, 3, 4, 5])
print("\nKoşullu değiştirme:")
print("Orijinal:", arr)
yeni = np.where(arr > 3, arr * 2, arr)
print("3'ten büyük elemanlar 2 ile çarpıldı:", yeni)

# 7. İNDEKS HESAPLAMA
# ----------------

# nonzero kullanımı
arr = np.array([0, 1, 0, 2, 0, 3, 0, 4])
sifir_olmayan = np.nonzero(arr)
print("\nSıfır olmayan elemanların indeksleri:", sifir_olmayan[0])
print("Sıfır olmayan elemanlar:", arr[sifir_olmayan])

# argmax, argmin kullanımı
print("\nEn büyük elemanın indeksi:", np.argmax(arr))
print("En küçük elemanın indeksi:", np.argmin(arr))

"""
ÖZET
----
1. Boolean indeksleme koşullu seçim yapar
2. Fancy indeksleme indeks dizisiyle seçim yapar
3. Karışık indeksleme teknikleri birleştirilebilir
4. Gelişmiş dilimleme esnek seçim sağlar
5. İndeks maskeleme ve koşullu değiştirme güçlü araçlardır

İPUÇLARI
-------
1. Doğru indeksleme yöntemini seçin
2. Boyut uyumluluğuna dikkat edin
3. Kopyalama ve görünüm farkını anlayın
4. Performans için uygun yöntemi kullanın
5. Karmaşık indekslemede adım adım ilerleyin
""" 