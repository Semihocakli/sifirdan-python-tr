# Python'da Dosya İşlemleri
# =======================

"""
DOSYA İŞLEMLERİ NEDİR?
--------------------
Dosya işlemleri, bilgisayarınızdaki dosyaları:
1. Oluşturma
2. Okuma
3. Yazma
4. Güncelleme
5. Silme
gibi işlemleri yapmanızı sağlar.
"""

# 1. DOSYA AÇMA VE KAPATMA
# ----------------------
print("1. Temel Dosya İşlemleri:")

# Dosya açma modları:
# 'r': Okuma modu (varsayılan)
# 'w': Yazma modu (dosyayı siler ve yeniden oluşturur)
# 'a': Ekleme modu (dosyanın sonuna ekler)
# 'x': Özel oluşturma modu (dosya varsa hata verir)
# 'b': Binary mod
# 't': Text modu (varsayılan)
# '+': Okuma ve yazma modu

# Dosya oluşturma ve yazma
with open("ornek.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Merhaba, Dünya!\n")
    dosya.write("Python ile dosya işlemleri\n")

print("Dosya yazma işlemi tamamlandı.")

# Dosya okuma
print("\nDosya içeriği:")
with open("ornek.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)

# 2. FARKLI OKUMA YÖNTEMLERİ
# ------------------------
print("\n2. Farklı Okuma Yöntemleri:")

with open("ornek.txt", "r", encoding="utf-8") as dosya:
    # Tüm satırları liste olarak okuma
    satirlar = dosya.readlines()
    print("readlines() ile:", satirlar)
    
    # Dosya başına dön
    dosya.seek(0)
    
    # Satır satır okuma
    print("\nSatır satır okuma:")
    for satir in dosya:
        print(f"Satır: {satir.strip()}")

# 3. DOSYAYA EKLEME YAPMA
# ---------------------
print("\n3. Dosyaya Ekleme:")

with open("ornek.txt", "a", encoding="utf-8") as dosya:
    dosya.write("Bu satır sonradan eklendi.\n")

# Eklenen içeriği kontrol etme
with open("ornek.txt", "r", encoding="utf-8") as dosya:
    print("\nGüncellenmiş dosya içeriği:")
    print(dosya.read())

# 4. DOSYA YÖNETİMİ
# ---------------
import os
print("\n4. Dosya Yönetimi:")

# Dosya varlığını kontrol etme
dosya_adi = "ornek.txt"
if os.path.exists(dosya_adi):
    print(f"{dosya_adi} mevcut")
    
    # Dosya bilgileri
    boyut = os.path.getsize(dosya_adi)
    print(f"Dosya boyutu: {boyut} byte")
    
    # Dosya yolu bilgileri
    print(f"Tam yol: {os.path.abspath(dosya_adi)}")
    print(f"Dizin adı: {os.path.dirname(os.path.abspath(dosya_adi))}")

# 5. BINARY DOSYA İŞLEMLERİ
# -----------------------
print("\n5. Binary Dosya İşlemleri:")

# Binary dosya yazma
with open("binary_ornek.bin", "wb") as dosya:
    veri = bytes([65, 66, 67, 68, 69])  # ASCII: ABCDE
    dosya.write(veri)

# Binary dosya okuma
with open("binary_ornek.bin", "rb") as dosya:
    icerik = dosya.read()
    print(f"Binary içerik: {icerik}")
    print(f"Decode edilmiş içerik: {icerik.decode('ascii')}")

# 6. DOSYA VE DİZİN İŞLEMLERİ
# -------------------------
print("\n6. Dosya ve Dizin İşlemleri:")

# Dizin oluşturma
os.makedirs("test_dizini", exist_ok=True)

# Dizin içeriğini listeleme
print("\nMevcut dizin içeriği:")
for item in os.listdir("."):
    if os.path.isfile(item):
        print(f"Dosya: {item}")
    elif os.path.isdir(item):
        print(f"Dizin: {item}")

# 7. DOSYA GÜVENLİĞİ VE HATA YÖNETİMİ
# --------------------------------
print("\n7. Güvenli Dosya İşlemleri:")

def guvenli_dosya_oku(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            return dosya.read()
    except FileNotFoundError:
        return "Dosya bulunamadı!"
    except PermissionError:
        return "Dosya erişim izni yok!"
    except Exception as e:
        return f"Beklenmeyen hata: {e}"

# Test
print(guvenli_dosya_oku("var_olmayan_dosya.txt"))
print(guvenli_dosya_oku("ornek.txt"))

"""
DOSYA İŞLEMLERİ İPUÇLARI
----------------------
1. Her zaman 'with' bloğu kullanın (otomatik kapatma)
2. Uygun karakter kodlaması seçin (genelde utf-8)
3. Büyük dosyalar için satır satır okuma yapın
4. Binary dosyalar için 'b' modu kullanın
5. Hata yönetimi ekleyin

GÜVENLİK ÖNLEMLERİ
----------------
1. Kullanıcı girdilerini doğrulayın
2. Dosya izinlerini kontrol edin
3. Hassas bilgileri şifreleyin
4. Geçici dosyaları temizleyin
5. Yolları doğrulayın (path traversal saldırılarına karşı)

PERFORMANS İPUÇLARI
----------------
1. Büyük dosyaları parça parça işleyin
2. Binary mod kullanın (uygunsa)
3. Dosyaları gereksiz yere açık tutmayın
4. Buffer boyutunu optimize edin
5. Dosya işlemlerini minimize edin
""" 