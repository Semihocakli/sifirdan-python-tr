# NumPy Dizi Manipülasyonları
# =========================

"""
NumPy dizilerinin şeklini değiştirme, birleştirme, ayırma ve
yeniden düzenleme işlemleri için çeşitli fonksiyonlar sunar.
"""

import numpy as np

# 1. ŞEKİL DEĞİŞTİRME
# ------------------

# Örnek dizi
arr = np.arange(12)  # 0'dan 11'e kadar sayılar
print("Orijinal dizi:", arr)

# reshape ile yeniden şekillendirme
matris = arr.reshape(3, 4)  # 3x4 matris
print("\nYeniden şekillendirilmiş (3x4):\n", matris)

# Düzleştirme (flatten)
duz = matris.flatten()
print("\nDüzleştirilmiş:", duz)

# 2. DİZİ BİRLEŞTİRME
# -----------------

# Yatay birleştirme
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
yatay = np.hstack((a, b))
print("\nYatay birleştirme:", yatay)

# Dikey birleştirme
dikey = np.vstack((a, b))
print("\nDikey birleştirme:\n", dikey)

# Derinlemesine birleştirme (3B için)
c = np.array([[1], [2], [3]])
d = np.array([[4], [5], [6]])
derinlik = np.dstack((c, d))
print("\nDerinlemesine birleştirme:\n", derinlik)

# 3. DİZİ AYIRMA
# ------------

# Yatay ayırma
arr = np.array([1, 2, 3, 4, 5, 6])
sol, sag = np.hsplit(arr, 2)
print("\nYatay ayırma:")
print("Sol:", sol)
print("Sağ:", sag)

# Dikey ayırma
matris = np.array([[1, 2], [3, 4], [5, 6]])
ust, alt = np.vsplit(matris, 2)
print("\nDikey ayırma:")
print("Üst:\n", ust)
print("Alt:\n", alt)

# 4. EKSEN İŞLEMLERİ
# ----------------

# Eksen ekleme
arr = np.array([1, 2, 3])
genisletilmis = np.expand_dims(arr, axis=0)
print("\nEksen ekleme:\n", genisletilmis)

# Eksen silme
daraltilmis = np.squeeze(genisletilmis)
print("Eksen silme:", daraltilmis)

# 5. DİZİ DÖNDÜRME VE ÇEVİRME
# -------------------------

matris = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("\nDöndürme ve Çevirme:")
print("Orijinal:\n", matris)
print("\n90 derece döndürme:\n", np.rot90(matris))
print("\nYatay çevirme:\n", np.fliplr(matris))
print("\nDikey çevirme:\n", np.flipud(matris))

# 6. TEKRARLAMA
# ----------

# tile ile tekrarlama
arr = np.array([1, 2])
tekrar = np.tile(arr, 3)
print("\nTile ile tekrarlama:", tekrar)

# repeat ile tekrarlama
tekrar2 = np.repeat(arr, 3)
print("Repeat ile tekrarlama:", tekrar2)

# 7. YENİDEN BOYUTLANDIRMA
# ----------------------

# resize ile yeniden boyutlandırma
arr = np.array([1, 2, 3, 4])
yeni = np.resize(arr, (2, 3))  # Eksik elemanlar tekrar eder
print("\nResize ile yeniden boyutlandırma:\n", yeni)

"""
ÖZET
----
1. reshape ile dizilerin şekli değiştirilebilir
2. hstack, vstack ile diziler birleştirilebilir
3. hsplit, vsplit ile diziler ayrılabilir
4. expand_dims, squeeze ile boyut eklenip çıkarılabilir
5. rot90, flip ile diziler döndürülüp çevrilebilir

İPUÇLARI
-------
1. Şekil değiştirirken boyut uyumuna dikkat edin
2. Birleştirme işlemlerinde boyutları kontrol edin
3. Bellek verimliliği için view kullanmayı düşünün
4. Büyük dizilerde kopyalama işlemlerine dikkat edin
5. Uygun manipülasyon fonksiyonunu seçin
""" 