# Python'da Nesne Yönelimli Programlama (OOP)
# ======================================

"""
NESNE YÖNELİMLİ PROGRAMLAMA NEDİR?
--------------------------------
OOP, programlama mantığını nesneler üzerine kuran bir yaklaşımdır.
Temel prensipler:
1. Kapsülleme (Encapsulation)
2. Kalıtım (Inheritance)
3. Çok Biçimlilik (Polymorphism)
4. Soyutlama (Abstraction)
"""

# 1. SINIF OLUŞTURMA VE TEMEL KAVRAMLAR
# ----------------------------------

class Ogrenci:
    # Sınıf değişkeni (tüm nesneler için ortak)
    okul = "Python Akademi"
    
    # Yapıcı metod (Constructor)
    def __init__(self, ad, soyad, numara):
        # Örnek değişkenleri (instance variables)
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self._notlar = []  # Protected değişken
        self.__mezuniyet = None  # Private değişken
    
    # Instance metod
    def not_ekle(self, not_):
        self._notlar.append(not_)
    
    def ortalama_hesapla(self):
        return sum(self._notlar) / len(self._notlar) if self._notlar else 0
    
    # String temsili
    def __str__(self):
        return f"{self.ad} {self.soyad} ({self.numara})"
    
    # Representation temsili
    def __repr__(self):
        return f"Ogrenci('{self.ad}', '{self.soyad}', {self.numara})"

# Sınıfı kullanma
print("1. Temel Sınıf Kullanımı:")
ogrenci1 = Ogrenci("Ahmet", "Yılmaz", 101)
ogrenci1.not_ekle(85)
ogrenci1.not_ekle(90)
print(f"Öğrenci: {ogrenci1}")
print(f"Ortalama: {ogrenci1.ortalama_hesapla()}")

# 2. KALITIM (INHERITANCE)
# ----------------------
print("\n2. Kalıtım Örneği:")

class Kisi:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
    
    def tam_ad(self):
        return f"{self.ad} {self.soyad}"

class Ogretmen(Kisi):
    def __init__(self, ad, soyad, brans):
        super().__init__(ad, soyad)
        self.brans = brans
    
    def bilgi_ver(self):
        return f"{self.tam_ad()} - {self.brans} Öğretmeni"

class LiseOgrencisi(Ogrenci):
    def __init__(self, ad, soyad, numara, sinif):
        super().__init__(ad, soyad, numara)
        self.sinif = sinif
    
    def bilgi_ver(self):
        return f"{self.tam_ad()} - {self.sinif}. Sınıf Öğrencisi"
    
    def tam_ad(self):
        return f"{self.ad} {self.soyad}"

# Kalıtım örneği
ogretmen = Ogretmen("Ayşe", "Demir", "Matematik")
lise_ogrencisi = LiseOgrencisi("Mehmet", "Kaya", 102, 11)

print(ogretmen.bilgi_ver())
print(lise_ogrencisi.bilgi_ver())

# 3. ÇOKLU KALITIM
# --------------
print("\n3. Çoklu Kalıtım Örneği:")

class Sporcu:
    def __init__(self, spor_dali):
        self.spor_dali = spor_dali
    
    def antrenman_yap(self):
        return f"{self.spor_dali} antrenmanı yapılıyor"

class SporculiseOgrencisi(LiseOgrencisi, Sporcu):
    def __init__(self, ad, soyad, numara, sinif, spor_dali):
        LiseOgrencisi.__init__(self, ad, soyad, numara, sinif)
        Sporcu.__init__(self, spor_dali)
    
    def bilgi_ver(self):
        return f"{super().bilgi_ver()} ve {self.spor_dali} sporcusu"

sporcu_ogrenci = SporculiseOgrencisi("Ali", "Veli", 103, 10, "Basketbol")
print(sporcu_ogrenci.bilgi_ver())
print(sporcu_ogrenci.antrenman_yap())

# 4. SOYUT SINIFLAR VE METODLAR
# --------------------------
from abc import ABC, abstractmethod
print("\n4. Soyut Sınıf Örneği:")

class Sekil(ABC):
    @abstractmethod
    def alan_hesapla(self):
        pass
    
    @abstractmethod
    def cevre_hesapla(self):
        pass

class Dikdortgen(Sekil):
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik
    
    def alan_hesapla(self):
        return self.uzunluk * self.genislik
    
    def cevre_hesapla(self):
        return 2 * (self.uzunluk + self.genislik)

dikdortgen = Dikdortgen(5, 3)
print(f"Dikdörtgen Alanı: {dikdortgen.alan_hesapla()}")
print(f"Dikdörtgen Çevresi: {dikdortgen.cevre_hesapla()}")

# 5. PROPERTY DECORATOR
# ------------------
print("\n5. Property Decorator Örneği:")

class Calisan:
    def __init__(self, ad, maas):
        self._ad = ad
        self._maas = maas
    
    @property
    def ad(self):
        return self._ad
    
    @property
    def maas(self):
        return self._maas
    
    @maas.setter
    def maas(self, yeni_maas):
        if yeni_maas < 0:
            raise ValueError("Maaş negatif olamaz!")
        self._maas = yeni_maas

calisan = Calisan("Ayşe", 5000)
print(f"Çalışan: {calisan.ad}")
calisan.maas = 6000
print(f"Yeni Maaş: {calisan.maas}")

# 6. STATIC VE CLASS METODLARI
# -------------------------
print("\n6. Static ve Class Metod Örneği:")

class Matematik:
    PI = 3.14
    
    def __init__(self):
        self.sonuc = 0
    
    @staticmethod
    def kare_al(sayi):
        return sayi ** 2
    
    @classmethod
    def daire_alan(cls, yaricap):
        return cls.PI * yaricap ** 2

print(f"5'in karesi: {Matematik.kare_al(5)}")
print(f"Yarıçapı 3 olan dairenin alanı: {Matematik.daire_alan(3)}")

"""
NESNE YÖNELİMLİ PROGRAMLAMA PRENSİPLERİ
-------------------------------------
1. Kapsülleme (Encapsulation):
   - Veri ve metodları bir arada tutma
   - Erişim kontrolü (public, protected, private)
   - Veri gizleme ve güvenlik

2. Kalıtım (Inheritance):
   - Kod tekrarını önleme
   - Hiyerarşik yapı oluşturma
   - Çoklu kalıtım imkanı

3. Çok Biçimlilik (Polymorphism):
   - Aynı arayüz, farklı uygulamalar
   - Metod overriding
   - Duck typing

4. Soyutlama (Abstraction):
   - Karmaşıklığı gizleme
   - Soyut sınıflar ve metodlar
   - Interface benzeri yapılar

İYİ UYGULAMALAR
-------------
1. Sınıf isimleri büyük harfle başlamalı
2. Her sınıf tek bir sorumluluğa sahip olmalı
3. Kalıtım yerine kompozisyon tercih edilebilir
4. Private değişkenler gerekmedikçe kullanılmamalı
5. Property'ler veri doğrulama için kullanılmalı

PERFORMANS VE GÜVENLİK
--------------------
1. Çoklu kalıtımda diamond problem'e dikkat edin
2. Büyük sınıflar yerine küçük, odaklı sınıflar oluşturun
3. Gereksiz inheritance zincirlerinden kaçının
4. Property'lerin performans etkisini göz önünde bulundurun
5. Soyut sınıfları doğru kullanın
""" 