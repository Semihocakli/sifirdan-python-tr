# Python'da Döngüler (Loops)
# =======================

"""
DÖNGÜLER NEDİR?
--------------
Döngüler, belirli bir kod bloğunu birden fazla kez çalıştırmamızı sağlayan yapılardır.
Python'da iki temel döngü türü vardır:
1. for döngüsü: Belirli bir koleksiyon üzerinde veya belirli sayıda tekrar için kullanılır
2. while döngüsü: Bir koşul doğru olduğu sürece tekrar eder
"""

# 1. FOR DÖNGÜSÜ
# -------------

# 1.1 Sayılar üzerinde döngü
print("1.1 Sayılar üzerinde for döngüsü:")
for i in range(5):  # 0'dan 4'e kadar (5 hariç)
    print(f"Sayı: {i}")

# range fonksiyonunun farklı kullanımları
print("\nrange() fonksiyonu örnekleri:")
print("range(3, 7):", end=" ")  # 3'ten 6'ya kadar
for i in range(3, 7):
    print(i, end=" ")

print("\nrange(2, 10, 2):", end=" ")  # 2'den 9'a kadar 2'şer artarak
for i in range(2, 10, 2):
    print(i, end=" ")

# 1.2 Liste üzerinde döngü
print("\n\n1.2 Liste üzerinde for döngüsü:")
meyveler = ["elma", "armut", "muz", "kiraz"]
for meyve in meyveler:
    print(f"Meyve: {meyve}")

# 1.3 Enumerate kullanımı (index ile birlikte)
print("\n1.3 Enumerate kullanımı:")
for index, meyve in enumerate(meyveler):
    print(f"{index}. index: {meyve}")

# 1.4 Sözlük (dictionary) üzerinde döngü
print("\n1.4 Sözlük üzerinde for döngüsü:")
kisi = {
    "ad": "Ahmet",
    "yas": 25,
    "sehir": "İstanbul"
}

# Sadece anahtarlar üzerinde döngü
print("Anahtarlar:")
for anahtar in kisi.keys():
    print(anahtar)

# Sadece değerler üzerinde döngü
print("\nDeğerler:")
for deger in kisi.values():
    print(deger)

# Hem anahtar hem değer üzerinde döngü
print("\nAnahtar-Değer çiftleri:")
for anahtar, deger in kisi.items():
    print(f"{anahtar}: {deger}")

# 2. WHILE DÖNGÜSÜ
# ---------------

# 2.1 Temel while döngüsü
print("\n2.1 Temel while döngüsü:")
sayac = 0
while sayac < 5:
    print(f"Sayaç: {sayac}")
    sayac += 1

# 2.2 break kullanımı (döngüyü sonlandırma)
print("\n2.2 break kullanımı:")
sayac = 0
while True:  # Sonsuz döngü
    print(f"Sayaç: {sayac}")
    sayac += 1
    if sayac >= 5:
        print("Döngüden çıkılıyor...")
        break

# 2.3 continue kullanımı (döngünün geri kalanını atlama)
print("\n2.3 continue kullanımı:")
for i in range(5):
    if i == 2:
        print("2 sayısı atlanıyor...")
        continue
    print(f"Sayı: {i}")

# 3. İÇ İÇE DÖNGÜLER
# -----------------
print("\n3. İç İçe Döngüler:")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# 4. DÖNGÜ İLE LİSTE OLUŞTURMA (List Comprehension)
# ----------------------------------------------
print("\n4. Liste Oluşturma Örnekleri:")

# Normal yöntem
kareler = []
for i in range(5):
    kareler.append(i ** 2)
print("Normal yöntem ile kareler:", kareler)

# List comprehension yöntemi
kareler_comp = [i ** 2 for i in range(5)]
print("List comprehension ile kareler:", kareler_comp)

# Koşullu list comprehension
cift_sayilar = [i for i in range(10) if i % 2 == 0]
print("Çift sayılar:", cift_sayilar)

"""
ALIŞTIRMALAR
-----------
1. 1'den 100'e kadar olan sayıların toplamını hesaplayan program
2. Bir listenin içindeki çift sayıları bulan program
3. Çarpım tablosu oluşturan program
"""

# Alıştırma 1: Sayıların Toplamı
print("\nAlıştırma 1 - Sayıların Toplamı:")
toplam = 0
for sayi in range(1, 101):
    toplam += sayi
print(f"1'den 100'e kadar olan sayıların toplamı: {toplam}")

# Alıştırma 2: Çift Sayıları Bulma
print("\nAlıştırma 2 - Çift Sayıları Bulma:")
sayilar = [1, 3, 4, 6, 8, 9, 12, 15, 17, 18]
cift_sayilar = []
for sayi in sayilar:
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)
print(f"Çift sayılar: {cift_sayilar}")

# Alıştırma 3: Çarpım Tablosu
print("\nAlıştırma 3 - Çarpım Tablosu:")
for i in range(1, 6):  # 1'den 5'e kadar
    for j in range(1, 6):  # 1'den 5'e kadar
        print(f"{i} x {j} = {i * j}")
    print("-" * 15)  # Ayırıcı çizgi

"""
ÖZET VE İYİ UYGULAMALAR
-----------------------
1. for döngüsü belirli bir koleksiyon üzerinde veya belirli sayıda tekrar için kullanılır
2. while döngüsü bir koşul doğru olduğu sürece tekrar eder
3. break ile döngüden çıkılabilir
4. continue ile döngünün o adımı atlanabilir
5. List comprehension ile tek satırda liste oluşturulabilir
6. İç içe döngüler kullanılabilir, ancak performans için dikkatli olunmalıdır
7. Sonsuz döngülerden kaçınılmalıdır
""" 
