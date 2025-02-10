# NumPy Lineer Cebir İşlemleri
# ==========================

"""
NumPy, lineer cebir işlemleri için güçlü fonksiyonlar sunar.
Matris işlemleri, determinant hesaplama, özdeğer ve özvektör bulma gibi
işlemler kolayca yapılabilir.
"""

import numpy as np
from numpy.linalg import inv, det, eig, solve

# 1. MATRİS İŞLEMLERİ
# -----------------

# Örnek matrisler
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matris A:\n", A)
print("\nMatris B:\n", B)

# Temel matris işlemleri
print("\nTemel Matris İşlemleri:")
print("Toplama:\n", A + B)
print("\nÇıkarma:\n", A - B)
print("\nMatris çarpımı:\n", np.dot(A, B))  # veya A @ B
print("\nTranspoz:\n", A.T)

# 2. ÖZEL MATRİSLER
# ---------------

print("\nÖzel Matrisler:")
print("Birim matris:\n", np.eye(3))
print("\nSıfır matris:\n", np.zeros((2, 2)))
print("\nBir matris:\n", np.ones((2, 2)))
print("\nDiyagonal matris:\n", np.diag([1, 2, 3]))

# 3. MATRİS ÖZELLİKLERİ
# -------------------

print("\nMatris Özellikleri:")
print("Determinant:", det(A))
print("İz (Trace):", np.trace(A))
print("Rank:", np.linalg.matrix_rank(A))
print("Boyut:", A.shape)

# 4. MATRİS AYRIŞTIRILMASI
# ----------------------

# Özdeğer ve özvektörler
eigenvalues, eigenvectors = eig(A)
print("\nÖzdeğer ve Özvektörler:")
print("Özdeğerler:", eigenvalues)
print("Özvektörler:\n", eigenvectors)

# Tekil değer ayrışımı (SVD)
U, s, Vh = np.linalg.svd(A)
print("\nTekil Değer Ayrışımı (SVD):")
print("U:\n", U)
print("Tekil değerler:", s)
print("Vh:\n", Vh)

# 5. DOĞRUSAL DENKLEM SİSTEMLERİ
# ---------------------------

# Ax = b denklem sistemi
A = np.array([[2, 1], [1, 3]])
b = np.array([4, 5])

print("\nDoğrusal Denklem Sistemi:")
print("A:\n", A)
print("b:", b)

# Çözüm
x = solve(A, b)
print("Çözüm (x):", x)

# Doğrulama
print("Doğrulama (Ax):", A @ x)

# 6. MATRİS NORMLAR
# --------------

print("\nMatris Normları:")
print("Frobenius normu:", np.linalg.norm(A, 'fro'))
print("L1 normu:", np.linalg.norm(A, 1))
print("L2 normu:", np.linalg.norm(A, 2))
print("Sonsuz normu:", np.linalg.norm(A, np.inf))

# 7. MATRİS İŞLEVLERİ
# ----------------

print("\nMatris İşlevleri:")
print("Üstel:\n", np.exp(A))
print("\nLogaritma:\n", np.log(np.abs(A)))
print("\nKarekök:\n", np.sqrt(np.abs(A)))

"""
ÖZET
----
1. NumPy temel matris işlemlerini destekler
2. Özel matrisler kolayca oluşturulabilir
3. Matris özellikleri hesaplanabilir
4. Matris ayrıştırma işlemleri yapılabilir
5. Doğrusal denklem sistemleri çözülebilir

İPUÇLARI
-------
1. Matris boyutlarına dikkat edin
2. Sayısal kararlılık için uygun yöntemleri seçin
3. Büyük matrislerde bellek kullanımına dikkat edin
4. Seyrek matrisler için scipy.sparse kullanın
5. Matris işlemlerinde @ operatörünü tercih edin
""" 