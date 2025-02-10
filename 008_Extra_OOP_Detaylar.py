# Python'da İleri Seviye OOP Kavramları
# =================================

"""
Bu dosyada OOP'nin daha ileri seviye konularını ve özellikle:
1. Özel metodlar (__init__, __str__, __len__ vb.)
2. Property ve Descriptor protokolü
3. Sınıf kompozisyonu
4. Mixin sınıfları
5. Meta sınıflar
konularını ele alacağız.
"""

# 1. ÖZEL METODLAR (MAGIC/DUNDER METHODS)
# ------------------------------------
print("1. Özel Metodlar Örneği:")

class Nokta:
    # Nesne oluşturulduğunda çağrılır, başlangıç değerlerini ayarlar
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # print() fonksiyonu kullanıldığında çağrılır, kullanıcı dostu string döndürür
    def __str__(self):
        return f"Nokta({self.x}, {self.y})"
    
    # Nesnenin detaylı string temsilini döndürür, debug için kullanılır
    def __repr__(self):
        return f"Nokta(x={self.x}, y={self.y})"
    
    # + operatörü kullanıldığında çağrılır (n1 + n2)
    def __add__(self, other):
        return Nokta(self.x + other.x, self.y + other.y)
    
    # == operatörü kullanıldığında çağrılır (n1 == n2)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # < operatörü kullanıldığında çağrılır (n1 < n2)
    def __lt__(self, other):
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
    
    # len() fonksiyonu kullanıldığında çağrılır
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)
    
    # Köşeli parantez notasyonu kullanıldığında çağrılır (nokta['x'])
    def __getitem__(self, key):
        if key == 'x':
            return self.x
        elif key == 'y':
            return self.y
        raise KeyError(f"Geçersiz anahtar: {key}")

# Özel metodların kullanımı
n1 = Nokta(3, 4)
n2 = Nokta(1, 2)
print(f"n1: {n1}")  # __str__
print(f"n1 + n2: {n1 + n2}")  # __add__
print(f"n1 == n2: {n1 == n2}")  # __eq__
print(f"n1 < n2: {n1 < n2}")  # __lt__
print(f"len(n1): {len(n1)}")  # __len__
print(f"n1['x']: {n1['x']}")  # __getitem__

# 2. GELİŞMİŞ PROPERTY VE DESCRIPTOR PROTOKOLÜ
# ----------------------------------------
print("\n2. Gelişmiş Property ve Descriptor Örneği:")

class Pozitif:
    """Bir descriptor sınıfı - pozitif sayıları kontrol eder"""
    
    def __init__(self):
        self._name = None
    
    # Sınıf oluşturulduğunda özellik ismi atanır
    def __set_name__(self, owner, name):
        self._name = name
    
    # Özellik değeri okunduğunda çağrılır
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]
    
    # Özelliğe değer atandığında çağrılır
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self._name} pozitif olmalıdır!")
        instance.__dict__[self._name] = value

class Dikdortgen:
    # Descriptor kullanımı - otomatik pozitif sayı kontrolü yapar
    uzunluk = Pozitif()
    genislik = Pozitif()
    
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik
    
    # Salt okunur özellik - hesaplanmış değer döndürür
    @property
    def alan(self):
        return self.uzunluk * self.genislik
    
    # Salt okunur özellik - hesaplanmış değer döndürür
    @property
    def cevre(self):
        return 2 * (self.uzunluk + self.genislik)
    
    # Property ile getter, setter ve deleter örnekleri
    def get_uzunluk(self):
        return self._uzunluk
    
    def set_uzunluk(self, value):
        if value <= 0:
            raise ValueError("Uzunluk pozitif olmalıdır!")
        self._uzunluk = value
    
    def del_uzunluk(self):
        del self._uzunluk
    
    # Property alternatif kullanımı - dekoratör yerine property() fonksiyonu
    uzunluk_prop = property(get_uzunluk, set_uzunluk, del_uzunluk, "Uzunluk özelliği")

# Property kullanım örneği
d = Dikdortgen(5, 3)
print(f"Alan: {d.alan}")
print(f"Çevre: {d.cevre}")

# 3. SINIF KOMPOZİSYONU VE AGGREGATION
# ---------------------------------
print("\n3. Sınıf Kompozisyonu Örneği:")

# Bileşen sınıfı - Arabanın bir parçası
class Motor:
    def __init__(self, guç):
        self.guç = guç
    
    def calistir(self):
        return "Motor çalıştı!"

# Bileşen sınıfı - Arabanın bir parçası
class Tekerlekler:
    def __init__(self, sayi):
        self.sayi = sayi
    
    def hareket(self):
        return f"{self.sayi} tekerlek hareket ediyor!"

# Ana sınıf - Diğer sınıfları içerir (kompozisyon)
class Araba:
    def __init__(self, marka, model, motor_gucu, tekerlek_sayisi):
        self.marka = marka
        self.model = model
        # Kompozisyon - Araba, Motor ve Tekerlekler'i içerir
        self.motor = Motor(motor_gucu)
        self.tekerlekler = Tekerlekler(tekerlek_sayisi)
    
    def bilgi_ver(self):
        return f"{self.marka} {self.model}\nMotor Gücü: {self.motor.guç}\nTekerlek Sayısı: {self.tekerlekler.sayi}"

araba = Araba("Toyota", "Corolla", 120, 4)
print(araba.bilgi_ver())
print(araba.motor.calistir())
print(araba.tekerlekler.hareket())

# 4. MIXIN SINIFLARI
# ---------------
print("\n4. Mixin Sınıfları Örneği:")

# Mixin sınıfı - JSON dönüşüm özelliği ekler
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

# Mixin sınıfı - Loglama özelliği ekler
class LogMixin:
    def log(self, message):
        print(f"[LOG] {message}")

# Ana sınıf - Mixin'leri kullanır
class Urun(JSONMixin, LogMixin):
    def __init__(self, ad, fiyat):
        self.ad = ad
        self.fiyat = fiyat
    
    def fiyat_guncelle(self, yeni_fiyat):
        eski_fiyat = self.fiyat
        self.fiyat = yeni_fiyat
        self.log(f"{self.ad} ürününün fiyatı {eski_fiyat}'dan {yeni_fiyat}'a güncellendi")

urun = Urun("Laptop", 5000)
print(f"JSON: {urun.to_json()}")
urun.fiyat_guncelle(5500)

# 5. META SINIFLAR
# -------------
print("\n5. Meta Sınıflar Örneği:")

# Meta sınıf - Singleton tasarım desenini uygular
class SingletonMeta(type):
    _instances = {}
    
    # Sınıftan yeni bir nesne oluşturulduğunda çağrılır
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# Singleton sınıf - Her zaman aynı nesneyi döndürür
class Veritabani(metaclass=SingletonMeta):
    def __init__(self):
        self.baglanti = "DB Bağlantısı kuruldu"
    
    def sorgu_calistir(self, sorgu):
        return f"Sorgu çalıştırılıyor: {sorgu}"

# Singleton test
db1 = Veritabani()
db2 = Veritabani()
print(f"db1 ve db2 aynı nesne mi? {db1 is db2}")

"""
GELİŞMİŞ OOP KAVRAMLARI VE İPUÇLARI
---------------------------------

1. Özel Metodlar:
   - __new__: Nesne oluşturmadan önce çağrılır, nesne oluşturma kontrolü sağlar
   - __init__: Nesne oluşturulduktan sonra başlatma işlemlerini yapar
   - __del__: Nesne silinmeden önce temizlik işlemleri için çağrılır
   - __call__: Nesneyi fonksiyon gibi çağırılabilir yapar
   - __enter__, __exit__: Context manager protokolünü uygular (with bloğu)
   - __getattr__, __setattr__: Özellik erişimini ve atamasını kontrol eder
   - __getitem__, __setitem__: Dizi benzeri erişimi sağlar

2. Property Kullanımı:
   - @property: Özelliği salt okunur yapar
   - @x.setter: Özelliğe değer atamayı kontrol eder
   - @x.deleter: Özelliği silme işlemini kontrol eder
   - Descriptor: Özellik davranışını özelleştirir
   - Veri doğrulama: Değer kontrolü sağlar

3. Sınıf Organizasyonu:
   - Kompozisyon: Has-a ilişkisi (Araba has-a Motor)
   - Mixin: Ek özellikler ekler
   - ABC: Soyut sınıflar ve metodlar
   - Interface: Davranış tanımlama
   - Meta: Sınıf davranışını özelleştirme

4. Bellek ve Performans:
   - __slots__: Bellek kullanımını azaltır
   - weakref: Zayıf referanslar oluşturur
   - Nesne havuzu: Nesne yeniden kullanımı
   - Önbellek: Hesaplama sonuçlarını saklar

5. İyi Uygulamalar:
   - SOLID: Yazılım tasarım prensipleri
   - DRY: Kod tekrarından kaçınma
   - KISS: Basit ve anlaşılır kod
   - Composition: Kalıtım yerine kompozisyon
   - Interface: Küçük ve odaklı arayüzler

PERFORMANS OPTİMİZASYONLARI
-------------------------
1. __slots__ ile bellek kullanımını optimize edin
2. Property'leri sadece gerektiğinde kullanın
3. Derin kalıtım zincirlerinden kaçının
4. Meta sınıfları dikkatli kullanın
5. Büyük sınıfları parçalara ayırın

GÜVENLİK ÖNLEMLERİ
----------------
1. Property ile veri doğrulama yapın
2. Private değişkenleri gerektiğinde kullanın
3. Immutable nesneler tercih edin
4. Exception handling kullanın
5. Input validasyonu yapın
""" 