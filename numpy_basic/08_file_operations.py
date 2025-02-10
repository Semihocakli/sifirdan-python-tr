# NumPy Dosya İşlemleri
# ===================

"""
NumPy, dizileri farklı formatlarda dosyalara kaydetme ve
dosyalardan okuma işlemleri için çeşitli fonksiyonlar sunar.
"""

import numpy as np
import os

# 1. NUMPY FORMATI (.npy)
# --------------------

# Örnek dizi oluşturma
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Orijinal dizi:\n", arr)

# Diziyi .npy formatında kaydetme
np.save('dizi.npy', arr)
print("\nDizi 'dizi.npy' olarak kaydedildi")

# Diziyi .npy dosyasından okuma
yuklenen = np.load('dizi.npy')
print("\nYüklenen dizi:\n", yuklenen)

# 2. SIKIŞTIRILMIŞ NUMPY FORMATI (.npz)
# ---------------------------------

# Birden fazla diziyi sıkıştırılmış formatta kaydetme
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
np.savez('diziler.npz', x=x, y=y)
print("\nDiziler 'diziler.npz' olarak kaydedildi")

# Sıkıştırılmış dosyadan okuma
veriler = np.load('diziler.npz')
print("\nYüklenen x dizisi:", veriler['x'])
print("Yüklenen y dizisi:", veriler['y'])

# 3. TEXT DOSYASI İŞLEMLERİ
# ----------------------

# Diziyi text dosyasına kaydetme
np.savetxt('dizi.txt', arr, fmt='%d', delimiter=',')
print("\nDizi 'dizi.txt' olarak kaydedildi")

# Text dosyasından okuma
yuklenen_txt = np.loadtxt('dizi.txt', delimiter=',')
print("\nText dosyasından yüklenen dizi:\n", yuklenen_txt)

# 4. CSV DOSYASI İŞLEMLERİ
# ---------------------

# CSV dosyası oluşturma ve kaydetme
veri = np.array([[1, 2, 3], [4, 5, 6]])
basliklar = 'A,B,C'
np.savetxt('veri.csv', veri, delimiter=',', header=basliklar)
print("\nVeri 'veri.csv' olarak kaydedildi")

# CSV dosyasından okuma (başlıkları atlayarak)
yuklenen_csv = np.loadtxt('veri.csv', delimiter=',', skiprows=1)
print("\nCSV'den yüklenen veri:\n", yuklenen_csv)

# 5. BINARY DOSYA İŞLEMLERİ
# ----------------------

# Binary formatta kaydetme
arr.tofile('dizi.bin')
print("\nDizi binary formatta kaydedildi")

# Binary dosyadan okuma
yuklenen_bin = np.fromfile('dizi.bin', dtype=np.int64)
yuklenen_bin = yuklenen_bin.reshape(3, 3)  # Orijinal şekle dönüştürme
print("\nBinary dosyadan yüklenen dizi:\n", yuklenen_bin)

# 6. DOSYA İŞLEMLERİ İÇİN YARDIMCI FONKSİYONLAR
# ----------------------------------------

def dosya_bilgisi(dosya_adi):
    """Dosya hakkında bilgi verir."""
    boyut = os.path.getsize(dosya_adi)
    uzanti = os.path.splitext(dosya_adi)[1]
    print(f"\nDosya: {dosya_adi}")
    print(f"Boyut: {boyut} bytes")
    print(f"Uzantı: {uzanti}")

# Dosya bilgilerini göster
for dosya in ['dizi.npy', 'diziler.npz', 'dizi.txt', 'veri.csv', 'dizi.bin']:
    dosya_bilgisi(dosya)

# Temizlik: Oluşturulan dosyaları sil
for dosya in ['dizi.npy', 'diziler.npz', 'dizi.txt', 'veri.csv', 'dizi.bin']:
    os.remove(dosya)
print("\nOluşturulan dosyalar temizlendi")

"""
ÖZET
----
1. NumPy kendi özel formatını (.npy, .npz) destekler
2. Text ve CSV dosyaları ile çalışılabilir
3. Binary format hızlı okuma/yazma sağlar
4. Farklı formatlar farklı avantajlar sunar
5. Dosya işlemlerinde hata kontrolü önemlidir

İPUÇLARI
-------
1. Büyük veriler için binary format kullanın
2. Okunabilirlik önemliyse text/CSV tercih edin
3. Sıkıştırma gerekiyorsa .npz kullanın
4. Dosya boyutlarına dikkat edin
5. Hata yönetimi ekleyin
""" 