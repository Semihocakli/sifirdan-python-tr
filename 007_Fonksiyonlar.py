# Python'da Fonksiyonlar
# ===================

"""
FONKSİYONLAR NEDİR?
------------------
Fonksiyonlar, belirli bir görevi yerine getiren ve tekrar kullanılabilen kod bloklarıdır.
Fonksiyonlar sayesinde:
1. Kod tekrarından kaçınırız
2. Programı modüler hale getiririz
3. Kodun okunabilirliğini artırırız
4. Bakım ve güncellemeyi kolaylaştırırız
"""

# 1. TEMEL FONKSİYON YAPISI
# ------------------------

# 1.1 Parametresiz Fonksiyon
def merhaba():
    print("Merhaba, Dünya!")

print("1.1 Parametresiz Fonksiyon:")
merhaba()

# 1.2 Parametreli Fonksiyon
def selamla(isim):
    print(f"Merhaba, {isim}!")

print("\n1.2 Parametreli Fonksiyon:")
selamla("Ahmet")

# 1.3 Varsayılan Parametreli Fonksiyon
def selam_ver(isim="Dostum"):
    print(f"Selam, {isim}!")

print("\n1.3 Varsayılan Parametreli Fonksiyon:")
selam_ver()          # Varsayılan değer kullanılır
selam_ver("Ayşe")    # Varsayılan değer yerine "Ayşe" kullanılır

# 2. DEĞER DÖNDÜREN FONKSİYONLAR
# ----------------------------

# 2.1 Tek Değer Döndürme
def kare_al(sayi):
    return sayi ** 2

print("\n2.1 Tek Değer Döndürme:")
sonuc = kare_al(5)
print(f"5'in karesi: {sonuc}")

# 2.2 Çoklu Değer Döndürme
def geometrik_hesapla(yaricap):
    cevre = 2 * 3.14 * yaricap
    alan = 3.14 * yaricap ** 2
    return cevre, alan

print("\n2.2 Çoklu Değer Döndürme:")
cevre, alan = geometrik_hesapla(3)
print(f"Dairenin çevresi: {cevre:.2f}")
print(f"Dairenin alanı: {alan:.2f}")

# 3. PARAMETRE TÜRLERİ
# ------------------

# 3.1 Pozisyonel ve İsimli Parametreler
def ogrenci_bilgi(ad, soyad, numara):
    print(f"Ad: {ad}, Soyad: {soyad}, Numara: {numara}")

print("\n3.1 Pozisyonel ve İsimli Parametreler:")
# Pozisyonel parametreler
ogrenci_bilgi("Ali", "Yılmaz", 123)
# İsimli parametreler
ogrenci_bilgi(numara=456, ad="Ayşe", soyad="Demir")

# 3.2 Değişken Sayıda Parametre
def toplam(*sayilar):
    return sum(sayilar)

def ogrenci_detay(**bilgiler):
    for anahtar, deger in bilgiler.items():
        print(f"{anahtar}: {deger}")

print("\n3.2 Değişken Sayıda Parametre:")
print(f"Toplam: {toplam(1, 2, 3, 4, 5)}")
print("\nÖğrenci Detayları:")
ogrenci_detay(ad="Mehmet", yas=20, bolum="Bilgisayar", sehir="İstanbul")

# 4. FONKSİYON İÇİNDE FONKSİYON
# ---------------------------

def dis_fonksiyon(x):
    def ic_fonksiyon(y):
        return x + y
    return ic_fonksiyon

print("\n4. Fonksiyon İçinde Fonksiyon:")
f = dis_fonksiyon(5)
print(f"Sonuç: {f(3)}")  # 5 + 3 = 8

# 5. LAMBDA FONKSİYONLARI
# ---------------------
print("\n5. Lambda Fonksiyonları:")

# Normal fonksiyon
def kare(x): return x ** 2

# Lambda ile aynı fonksiyon
kare_lambda = lambda x: x ** 2

print(f"Normal fonksiyon: {kare(4)}")
print(f"Lambda fonksiyon: {kare_lambda(4)}")

# Lambda kullanım örneği
sayilar = [1, 2, 3, 4, 5]
kareler = list(map(lambda x: x**2, sayilar))
print(f"Sayıların kareleri: {kareler}")

# 6. RECURSIVE (ÖZYİNELEMELİ) FONKSİYONLAR
# -------------------------------------

def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    return n * faktoriyel(n-1)

print("\n6. Recursive Fonksiyonlar:")
print(f"5! = {faktoriyel(5)}")

# 7. GENERATOR FONKSİYONLAR
# -----------------------

def sayilar_generator():
    n = 1
    while n <= 5:
        yield n
        n += 1

print("\n7. Generator Fonksiyonlar:")
for sayi in sayilar_generator():
    print(sayi, end=" ")

# 8. DEKORATÖRLER
# -------------

def log_decorator(func):
    def wrapper():
        print("\nFonksiyon başlıyor...")
        func()
        print("Fonksiyon bitti...")
    return wrapper

@log_decorator
def selamla():
    print("Merhaba!")

print("\n\n8. Dekoratörler:")
selamla()

"""
FONKSİYON YAZMA PRENSİPLERİ
--------------------------
1. Tek Sorumluluk: Her fonksiyon tek bir işi yapmalıdır
2. İsimlendirilme: Fonksiyon isimleri açıklayıcı olmalıdır
3. Parametre Sayısı: Mümkünse az sayıda parametre kullanın
4. Dokümantasyon: Karmaşık fonksiyonlar için docstring kullanın
5. Return Değerleri: Return değerleri tutarlı olmalıdır

İYİ UYGULAMALAR
--------------
1. Fonksiyonlar mümkün olduğunca kısa olmalıdır
2. Global değişkenler yerine parametre kullanın
3. Hata kontrolü yapın
4. Fonksiyon içinde fonksiyon kullanımını sınırlı tutun
5. Recursive fonksiyonlarda taban durumu unutulmamalıdır

PERFORMANS İPUÇLARI
-----------------
1. Generator fonksiyonlar büyük veri setleri için uygundur
2. Lambda fonksiyonlar basit işlemler için idealdir
3. Recursive fonksiyonlar dikkatli kullanılmalıdır (stack overflow riski)
4. Parametre sayısı arttıkça performans düşebilir
5. Dekoratörler ek yük getirir, gereksiz kullanımdan kaçının
""" 