# Python'da Hata Yönetimi (Exception Handling)
# =====================================

"""
HATA YÖNETİMİ NEDİR?
------------------
Hata yönetimi, programın çalışması sırasında oluşabilecek hataları:
1. Öngörmemizi
2. Kontrol etmemizi
3. Uygun şekilde işlememizi
sağlayan mekanizmadır.
"""

# 1. TEMEL HATA YÖNETİMİ
# --------------------
print("1. Temel Hata Yönetimi Örneği:")

# try-except bloğu
try:
    sayi = int(input("Bir sayı girin: "))
    sonuc = 100 / sayi
    print(f"Sonuç: {sonuc}")
except ValueError:
    print("Geçerli bir sayı girmediniz!")
except ZeroDivisionError:
    print("Sıfıra bölme hatası!")
except:  # Genel hata yakalama (önerilmez)
    print("Beklenmeyen bir hata oluştu!")

# 2. ÇOKLU HATA YAKALAMA
# --------------------
print("\n2. Çoklu Hata Yakalama Örneği:")

def dosya_oku(dosya_adi):
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as dosya:
            icerik = dosya.read()
            sayilar = [int(sayi) for sayi in icerik.split()]
            return sum(sayilar) / len(sayilar)
    except FileNotFoundError:
        print(f"'{dosya_adi}' dosyası bulunamadı!")
    except (ValueError, TypeError):
        print("Dosya içeriği sayılara dönüştürülemedi!")
    except ZeroDivisionError:
        print("Dosya boş!")
    except Exception as e:
        print(f"Beklenmeyen hata: {str(e)}")
    finally:
        print("Dosya işlemleri tamamlandı.")

# Farklı senaryoları test edelim
dosya_oku("olmayan_dosya.txt")

# 3. ÖZEL HATA SINIFI OLUŞTURMA
# --------------------------
print("\n3. Özel Hata Sınıfı Örneği:")

class YasHatasi(Exception):
    """Yaş ile ilgili hataları yönetmek için özel hata sınıfı"""
    def __init__(self, mesaj="Geçersiz yaş değeri!"):
        self.mesaj = mesaj
        super().__init__(self.mesaj)

def yas_kontrol(yas):
    if not isinstance(yas, (int, float)):
        raise TypeError("Yaş sayısal bir değer olmalıdır!")
    if yas < 0:
        raise YasHatasi("Yaş negatif olamaz!")
    if yas > 150:
        raise YasHatasi("Yaş çok büyük!")
    return True

# Özel hata sınıfını test edelim
try:
    print("Yaş -5 kontrolü:")
    yas_kontrol(-5)
except YasHatasi as e:
    print(f"Hata: {e}")

try:
    print("\nYaş 200 kontrolü:")
    yas_kontrol(200)
except YasHatasi as e:
    print(f"Hata: {e}")

# 4. CONTEXT MANAGER KULLANIMI
# -------------------------
print("\n4. Context Manager Örneği:")

class DosyaYoneticisi:
    def __init__(self, dosya_adi, mod):
        self.dosya_adi = dosya_adi
        self.mod = mod
        self.dosya = None
    
    def __enter__(self):
        try:
            self.dosya = open(self.dosya_adi, self.mod)
            return self.dosya
        except Exception as e:
            print(f"Dosya açılırken hata: {e}")
            return None
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.dosya:
            self.dosya.close()
            print("Dosya başarıyla kapatıldı.")
        if exc_type is not None:
            print(f"Hata türü: {exc_type}")
            print(f"Hata mesajı: {exc_value}")
            return True  # Hatayı yakalar ve programın devam etmesini sağlar

# Context manager kullanımı
with DosyaYoneticisi("test.txt", "w") as dosya:
    if dosya:
        dosya.write("Merhaba, Dünya!")

# 5. ASSERT KULLANIMI
# ----------------
print("\n5. Assert Kullanımı:")

def ortalama_hesapla(notlar):
    assert len(notlar) > 0, "Not listesi boş olamaz!"
    assert all(0 <= not_ <= 100 for not_ in notlar), "Notlar 0-100 arasında olmalıdır!"
    return sum(notlar) / len(notlar)

# Assert kullanımını test edelim
try:
    notlar = [85, 90, 75, 95]
    print(f"Ortalama: {ortalama_hesapla(notlar)}")
    
    notlar = [85, 90, 150, 95]  # Geçersiz not
    print(f"Ortalama: {ortalama_hesapla(notlar)}")
except AssertionError as e:
    print(f"Doğrulama hatası: {e}")

"""
HATA YÖNETİMİ İPUÇLARI
--------------------
1. Spesifik Hatalar:
   - Genel 'except' bloğundan kaçının
   - Mümkün olduğunca spesifik hataları yakalayın
   - Hata mesajlarını açıklayıcı yapın

2. finally Kullanımı:
   - Kaynak temizleme için finally kullanın
   - Dosya, veritabanı bağlantıları gibi kaynakları kapatın
   - Context manager'ları tercih edin

3. Özel Hata Sınıfları:
   - Anlamlı hata sınıfları oluşturun
   - Hata mesajlarını özelleştirin
   - Hata hiyerarşisini doğru kullanın

4. Assert Kullanımı:
   - Geliştirme aşamasında hataları yakalayın
   - Ön koşulları kontrol edin
   - Üretim kodunda dikkatli kullanın

5. Hata Ayıklama:
   - try-except bloklarını gerektiği kadar küçük tutun
   - Hataları loglayın
   - Kullanıcıya anlaşılır mesajlar verin

GÜVENLİK ÖNLEMLERİ
----------------
1. Hassas bilgileri hata mesajlarında göstermeyin
2. Güvenlik açıklarına yol açabilecek hataları gizleyin
3. Kullanıcı girdilerini doğrulayın
4. Sistem kaynaklarını kontrollü kullanın
5. Hata loglarını güvenli şekilde saklayın

PERFORMANS İPUÇLARI
-----------------
1. try-except maliyetlidir, gereksiz kullanmayın
2. Büyük try bloklarından kaçının
3. Exception yerine daha spesifik hatalar kullanın
4. Context manager'ları tercih edin
5. Assert'leri üretim kodunda devre dışı bırakın
""" 