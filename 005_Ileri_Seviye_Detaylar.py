# Python İleri Seviye Detaylar
# =========================

"""
Bu dosyada, şimdiye kadar öğrendiğimiz konuların daha derin ve ileri seviye detaylarını inceleyeceğiz.
Aşağıdaki konular, bir Python uzmanı olma yolunda önemli detayları içermektedir.
"""

# 1. VERİ TİPLERİNİN DERİN DETAYLARI
# --------------------------------

# 1.1 Sayılar ve Bellek Yönetimi
# Python'da küçük tamsayılar için özel bir bellek optimizasyonu vardır
x = 5
y = 5
print("\n1.1 Sayılar ve Bellek:")
print(f"x ve y aynı nesneyi mi gösteriyor? {x is y}")  # True
# Python -5 ile 256 arasındaki sayıları önbelleğe alır

# Büyük sayılarda durum farklıdır
buyuk_sayi1 = 257
buyuk_sayi2 = 257
print(f"buyuk_sayi1 ve buyuk_sayi2 aynı nesneyi mi gösteriyor? {buyuk_sayi1 is buyuk_sayi2}")  # False

# 1.2 String İnternals
# Strings are immutable (değiştirilemez)
print("\n1.2 String Detayları:")
str1 = "Python"
print(f"String'in bellek adresi: {id(str1)}")
str1 = str1 + " Programming"  # Yeni bir string nesnesi oluşturulur
print(f"Değişiklik sonrası bellek adresi: {id(str1)}")

# String metodlarının detaylı kullanımı
metin = "   Python Programlama   "
print(f"Strip öncesi ve sonrası: '{metin}' -> '{metin.strip()}'")
print(f"Sol strip: '{metin.lstrip()}'")
print(f"Sağ strip: '{metin.rstrip()}'")
print(f"Bölme (split): {metin.split()}")
print(f"Değiştirme (replace): {metin.replace('Python', 'Java')}")

# 1.3 Liste İleri Seviye
print("\n1.3 Liste İleri Seviye:")

# Liste kopyalama yöntemleri ve farkları
liste1 = [1, [2, 3], 4]
liste2 = liste1  # Sığ kopya (shallow copy)
liste3 = liste1.copy()  # Yüzeysel kopya
import copy
liste4 = copy.deepcopy(liste1)  # Derin kopya

liste1[1][0] = 5
print(f"Orijinal liste: {liste1}")
print(f"Sığ kopya: {liste2}")
print(f"Yüzeysel kopya: {liste3}")
print(f"Derin kopya: {liste4}")

# Liste sıralama detayları
print("\nListe Sıralama Detayları:")
sayilar = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Normal sıralama: {sorted(sayilar)}")
print(f"Tersten sıralama: {sorted(sayilar, reverse=True)}")

# Özel nesneleri sıralama
class Ogrenci:
    def __init__(self, ad, not_ort):
        self.ad = ad
        self.not_ort = not_ort
    
    def __repr__(self):
        return f"{self.ad}({self.not_ort})"

ogrenciler = [
    Ogrenci("Ali", 85),
    Ogrenci("Veli", 90),
    Ogrenci("Ayşe", 95)
]

print("\nÖzel sıralama örnekleri:")
print(f"Not ortalamasına göre sıralama: {sorted(ogrenciler, key=lambda x: x.not_ort)}")
print(f"İsme göre sıralama: {sorted(ogrenciler, key=lambda x: x.ad)}")

# 2. KONTROL YAPILARI VE DÖNGÜLER - İLERİ SEVİYE
# -------------------------------------------

# 2.1 Koşul İfadelerinde Kısa Devre Değerlendirmesi (Short-Circuit Evaluation)
print("\n2.1 Kısa Devre Değerlendirmesi:")

def kontrol1():
    print("Kontrol 1 çalıştı")
    return False

def kontrol2():
    print("Kontrol 2 çalıştı")
    return True

print("AND operatörü ile:")
sonuc = kontrol1() and kontrol2()  # kontrol2 çalışmaz
print(f"Sonuç: {sonuc}")

print("\nOR operatörü ile:")
sonuc = kontrol2() or kontrol1()  # kontrol1 çalışmaz
print(f"Sonuç: {sonuc}")

# 2.2 İç İçe Döngülerde Optimizasyon
print("\n2.2 İç İçe Döngü Optimizasyonu:")

# Kötü performanslı kod
def kotu_performans(n):
    sonuc = []
    for i in range(n):
        for j in range(n):
            sonuc.append(i * j)
    return sonuc

# Daha iyi performanslı kod
def iyi_performans(n):
    return [i * j for i in range(n) for j in range(n)]

# 2.3 Generator İfadeleri
print("\n2.3 Generator İfadeleri:")

# Normal liste
liste_kareler = [x**2 for x in range(10)]  # Tüm değerler bellekte tutulur

# Generator (değerler talep edildikçe üretilir)
generator_kareler = (x**2 for x in range(10))

print(f"Liste bellekte: {liste_kareler}")
print(f"Generator objesi: {generator_kareler}")

# Generator kullanımı
for deger in generator_kareler:
    print(deger, end=" ")

# 3. PERFORMANS VE BELLEK OPTİMİZASYONU
# ----------------------------------

# 3.1 locals() ve globals() kullanımı
print("\n\n3.1 locals() ve globals():")
x = 10
def fonksiyon():
    y = 20
    print(f"Yerel değişkenler: {locals()}")
    print(f"Global değişkenler: {globals()['x']}")

fonksiyon()

# 3.2 Bellek kullanımını kontrol etme
import sys
print("\n3.2 Bellek Kullanımı:")
print(f"Integer'ın bellek kullanımı: {sys.getsizeof(0)} bytes")
print(f"String'in bellek kullanımı: {sys.getsizeof('')} bytes")
print(f"List'in bellek kullanımı: {sys.getsizeof([])} bytes")
print(f"Dict'in bellek kullanımı: {sys.getsizeof({})} bytes")

# 3.3 Performans İpuçları
print("\n3.3 Performans İpuçları:")

# Join kullanımı (string birleştirme için en etkili yöntem)
kelimeler = ["Python", "Programlama", "Dili"]
kotu_yontem = ""
for kelime in kelimeler:
    kotu_yontem += kelime + " "

iyi_yontem = " ".join(kelimeler)

print(f"Kötü yöntem: {kotu_yontem}")
print(f"İyi yöntem: {iyi_yontem}")

"""
ÖZET VE İLERİ SEVİYE İPUÇLARI
----------------------------
1. Python'da bellek yönetimi ve optimizasyon önemlidir
2. String işlemlerinde immutability kavramını anlamak kritiktir
3. Liste kopyalama işlemlerinde shallow ve deep copy farkını bilmek önemlidir
4. Performans için generator ifadelerini kullanmak avantajlıdır
5. Bellek kullanımını optimize etmek için uygun veri yapılarını seçmek önemlidir
6. String birleştirme işlemlerinde join metodunu tercih etmek daha verimlidir
7. Kısa devre değerlendirmesi mantıksal operatörlerde performansı etkiler

İLERİ SEVİYE KONULAR İÇİN ÖNERİLER
--------------------------------
1. Decorators (Dekoratörler)
2. Context Managers (with ifadeleri)
3. Metaclasses (Üst sınıflar)
4. Coroutines ve Asenkron Programlama
5. Memory Management ve Garbage Collection
6. Multi-threading ve Multi-processing
7. Design Patterns (Tasarım Kalıpları)
""" 