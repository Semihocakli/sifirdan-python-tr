# Python'da Modüller ve Paketler
# ==========================

"""
MODÜLLER VE PAKETLER NEDİR?
-------------------------
Modül: Değişkenler, fonksiyonlar ve sınıflar içeren Python dosyasıdır.
Paket: Birden fazla modülü organize eden dizin yapısıdır.

Modül ve paketler sayesinde:
1. Kodu organize edebiliriz
2. Kodu yeniden kullanabiliriz
3. İsim çakışmalarını önleyebiliriz
"""

# 1. MODÜL OLUŞTURMA VE KULLANMA
# ----------------------------

# matematik.py adında bir modül oluşturalım
def matematik_modulu_olustur():
    with open("matematik.py", "w", encoding="utf-8") as f:
        f.write('''
# matematik.py
def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        raise ValueError("Sıfıra bölme hatası!")
    return a / b

PI = 3.14159
E = 2.71828
''')

# Modülü oluşturalım
matematik_modulu_olustur()

# Modülü içe aktarma yöntemleri
print("1. Modül İçe Aktarma Örnekleri:")

# 1. Yöntem: Tüm modülü içe aktarma
import matematik
print(f"PI sayısı: {matematik.PI}")
print(f"3 + 5 = {matematik.topla(3, 5)}")

# 2. Yöntem: Belirli öğeleri içe aktarma
from matematik import topla, cikar
print(f"10 - 4 = {cikar(10, 4)}")

# 3. Yöntem: Takma ad kullanma
import matematik as mat
print(f"4 * 6 = {mat.carp(4, 6)}")

# 2. PAKET OLUŞTURMA
# ----------------
print("\n2. Paket Oluşturma Örneği:")

def hesaplamalar_paketi_olustur():
    import os
    
    # Ana paket dizini
    os.makedirs("hesaplamalar", exist_ok=True)
    
    # __init__.py dosyası (paketi tanımlar)
    with open("hesaplamalar/__init__.py", "w") as f:
        f.write('"""Hesaplamalar paketi"""\n')
    
    # Temel matematik modülü
    with open("hesaplamalar/temel.py", "w", encoding="utf-8") as f:
        f.write('''
def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b
''')
    
    # İleri matematik modülü
    with open("hesaplamalar/ileri.py", "w", encoding="utf-8") as f:
        f.write('''
import math

def karekok(x):
    return math.sqrt(x)

def us_al(x, y):
    return x ** y
''')

# Paketi oluşturalım
hesaplamalar_paketi_olustur()

# Paketi kullanma
from hesaplamalar import temel, ileri
print(f"15 + 5 = {temel.topla(15, 5)}")
print(f"16'nın karekökü = {ileri.karekok(16)}")

# 3. MODÜL VE PAKET YÖNETİMİ
# ------------------------
print("\n3. Modül ve Paket Yönetimi:")

# Modül arama yolu
import sys
print("Python modül arama yolları:")
for yol in sys.path:
    print(f"- {yol}")

# Modül bilgisi
import math
print("\nMath modülü hakkında bilgi:")
print(f"Modül dosyası: {math.__file__}")
print(f"Modül dokümanı:\n{math.__doc__}")

# 4. NAMESPACE VE KAPSAM
# -------------------
print("\n4. Namespace ve Kapsam Örneği:")

# Global namespace
x = 10

def fonksiyon():
    # Lokal namespace
    x = 20
    print(f"Lokal x: {x}")

print(f"Global x: {x}")
fonksiyon()
print(f"Fonksiyon sonrası global x: {x}")

# 5. MODÜL TASARIM PRENSİPLERİ
# -------------------------
print("\n5. Modül Tasarım Prensipleri Örneği:")

def ornek_modul_olustur():
    with open("ornek_modul.py", "w", encoding="utf-8") as f:
        f.write('''
"""
Bu modül örnek bir modül tasarımını gösterir.
Modül dokümanı modülün başında yer alır.
"""

# Dışa açık değişkenler (public)
VERSION = "1.0.0"
AUTHOR = "Python Kursu"

# İçsel kullanım için değişkenler (private)
_config = {
    "debug": False,
    "cache_size": 1000
}

# Dışa açık fonksiyonlar
def hesapla(x, y):
    """İki sayıyı toplar ve çarpar"""
    return _topla(x, y), _carp(x, y)

# İçsel fonksiyonlar
def _topla(a, b):
    return a + b

def _carp(a, b):
    return a * b

# Ana çalıştırma bloğu
if __name__ == "__main__":
    print("Bu modül doğrudan çalıştırıldı")
    print(hesapla(5, 3))
else:
    print("Bu modül içe aktarıldı")
''')

# Örnek modülü oluşturalım
ornek_modul_olustur()

"""
MODÜL VE PAKET TASARIM İPUÇLARI
-----------------------------
1. Modül Organizasyonu:
   - Her modül tek bir amaca hizmet etmeli
   - İlgili fonksiyonlar ve sınıflar bir arada olmalı
   - Modül isimleri açıklayıcı olmalı

2. Dokümantasyon:
   - Modül başında docstring kullanın
   - Fonksiyon ve sınıfları dokümante edin
   - Örnekler ve kullanım senaryoları ekleyin

3. İsimlendirme:
   - İçsel kullanım için '_' öneki kullanın
   - Sabit değişkenler büyük harfle yazılmalı
   - PEP 8 kurallarına uyun

4. Paket Yapısı:
   - __init__.py dosyasını unutmayın
   - Alt paketleri mantıklı gruplandırın
   - Döngüsel bağımlılıklardan kaçının

5. Performans:
   - Gereksiz import'lardan kaçının
   - Lazy loading kullanmayı düşünün
   - İçe aktarma sırasını optimize edin

GÜVENLİK ÖNLEMLERİ
----------------
1. Hassas bilgileri modüllerde saklamayın
2. Güvenlik açıklarına karşı kontroller ekleyin
3. Kullanıcı girdilerini doğrulayın
4. Hata yönetimini unutmayın
5. Bağımlılıkları güncel tutun

PERFORMANS İPUÇLARI
-----------------
1. Modülleri gerektiğinde yükleyin
2. Büyük modülleri parçalara ayırın
3. Önbelleğe alma mekanizmaları kullanın
4. Import yöntemini doğru seçin
5. Gereksiz global değişkenlerden kaçının
""" 