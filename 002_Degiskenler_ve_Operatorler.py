# Python'da Değişkenler ve Operatörler
# ================================

"""
DEĞİŞKENLER (Variables)
-----------------------
Değişkenler, programlama dillerinde veri depolamak için kullanılan yapılardır.
Python'da değişken oluştururken dikkat edilmesi gereken kurallar:

1. Değişken isimleri harf veya alt çizgi (_) ile başlamalıdır
2. Sayı ile başlayamaz ama içerebilir
3. Sadece harf, sayı ve alt çizgi içerebilir
4. Büyük/küçük harf duyarlıdır (case-sensitive)
5. Özel karakterler (!, @, #, $ vb.) kullanılamaz
6. Python'a özel kelimeleri (if, for, while vb.) kullanamayız
"""

# DOĞRU değişken isimlendirme örnekleri:
isim = "Ahmet"
yas = 25
_gizli_degisken = "gizli"
ogrenciNo123 = "12345"
MAKSIMUM_PUAN = 100  # Sabitler genelde büyük harfle yazılır
print(_gizli_degisken)

# YANLIŞ değişken isimlendirme örnekleri (bunları çalıştırmayacağız):
# 1sayi = 5        # Sayı ile başlayamaz
# öğrenci-no = 1   # Tire işareti kullanılamaz
# while = 3        # Python özel kelimesi kullanılamaz

"""
VERİ TİPLERİ (Data Types)
-------------------------
Python'da temel veri tipleri:
"""

# 1. Sayısal Veri Tipleri
tam_sayi = 42                    # int (Integer - Tam Sayı)
ondalikli_sayi = 3.14           # float (Float - Ondalıklı Sayı)
karmasik_sayi = 2 + 3j          # complex (Karmaşık Sayı)

# 2. Metin Veri Tipi
metin1 = 'Python'               # string (tek tırnak)
metin2 = "Programlama"          # string (çift tırnak)
uzun_metin = '''Bu bir
çok satırlı
metindir'''                     # çok satırlı string

# 3. Mantıksal Veri Tipi
dogru = True                    # boolean
yanlis = False                  # boolean

# 4. Sıralı Veri Tipleri
liste = [1, 2, 3]              # list (değiştirilebilir)
demet = (1, 2, 3)              # tuple (değiştirilemez)
kume = {1, 2, 3}               # set (benzersiz elemanlar)

# 5. Sözlük Veri Tipi
sozluk = {'anahtar': 'değer'}  # dictionary

# Veri tiplerini kontrol etme
print("\nVeri Tiplerini Kontrol Edelim:")
print(f"42'nin tipi: {type(tam_sayi)}")
print(f"3.14'ün tipi: {type(ondalikli_sayi)}")
print(f"'Python' kelimesinin tipi: {type(metin1)}")
print(f"True'nun tipi: {type(dogru)}")

"""
OPERATÖRLER (Operators)
----------------------
Python'da temel operatör türleri:
"""

# 1. Aritmetik Operatörler
print("\nAritmetik Operatörler:")
a, b = 10, 3
print(f"Toplama: {a} + {b} = {a + b}")         # Toplama
print(f"Çıkarma: {a} - {b} = {a - b}")         # Çıkarma
print(f"Çarpma: {a} * {b} = {a * b}")          # Çarpma
print(f"Bölme: {a} / {b} = {a / b}")           # Bölme (sonuç her zaman float)
print(f"Tam Bölme: {a} // {b} = {a // b}")     # Tam Bölme (sonuç tam sayı)
print(f"Mod Alma: {a} % {b} = {a % b}")        # Mod Alma (kalan)
print(f"Üs Alma: {a} ** {b} = {a ** b}")       # Üs Alma

# 2. Karşılaştırma Operatörleri
print("\nKarşılaştırma Operatörleri:")
print(f"{a} > {b}: {a > b}")    # Büyüktür
print(f"{a} < {b}: {a < b}")    # Küçüktür
print(f"{a} >= {b}: {a >= b}")  # Büyük eşittir
print(f"{a} <= {b}: {a <= b}")  # Küçük eşittir
print(f"{a} == {b}: {a == b}")  # Eşittir
print(f"{a} != {b}: {a != b}")  # Eşit değildir

# 3. Mantıksal Operatörler
print("\nMantıksal Operatörler:")
x, y = True, False
print(f"x and y: {x and y}")    # VE (and)
print(f"x or y: {x or y}")      # VEYA (or)
print(f"not x: {not x}")        # DEĞİL (not)

# 4. Atama Operatörleri
sayi = 5                # Basit atama
sayi += 3              # sayi = sayi + 3
sayi -= 2              # sayi = sayi - 2
sayi *= 4              # sayi = sayi * 4
sayi /= 2              # sayi = sayi / 2
print(f"\nAtama operatörleri sonucu: {sayi}")

"""
TİP DÖNÜŞÜMLERİ (Type Conversion)
--------------------------------
Python'da bir veri tipinden başka bir veri tipine dönüşüm yapabiliriz:
"""

# String'den sayıya dönüşüm
sayi_metin = "123"
sayi_int = int(sayi_metin)      # String'den integer'a
sayi_float = float(sayi_metin)  # String'den float'a

# Sayıdan string'e dönüşüm
sayi = 456
metin = str(sayi)               # Sayıdan string'e

print("\nTip Dönüşümleri:")
print(f"String '123' -> int: {sayi_int}, tipi: {type(sayi_int)}")
print(f"String '123' -> float: {sayi_float}, tipi: {type(sayi_float)}")
print(f"Integer 456 -> string: {metin}, tipi: {type(metin)}")

"""
ÖZET
----
1. Değişkenler veri depolamak için kullanılır
2. Python'da değişken isimlendirme kuralları önemlidir
3. Farklı veri tipleri farklı amaçlar için kullanılır
4. Operatörler değişkenler üzerinde işlem yapmamızı sağlar
5. Tip dönüşümleri ile veri tipleri arasında geçiş yapabiliriz
""" 