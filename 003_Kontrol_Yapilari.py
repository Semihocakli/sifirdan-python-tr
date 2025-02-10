# Python'da Kontrol Yapıları (Control Structures)
# =========================================

"""
KONTROL YAPILARI NEDİR?
-----------------------
Kontrol yapıları, programın akışını yönlendiren ve belirli koşullara göre
farklı kod bloklarının çalıştırılmasını sağlayan yapılardır.

Python'da temel kontrol yapıları:
1. if (eğer)
2. elif (değilse eğer)
3. else (değilse)
"""

# 1. TEMEL IF YAPISI
# ------------------
print("1. Temel if Yapısı Örneği:")
yas = 18

if yas >= 18:
    print("Reşitsiniz!")
    print("Ehliyet alabilirsiniz.")

"""
ÖNEMLİ NOT: Python'da girintiler (indentation) çok önemlidir!
if bloğuna ait kodlar mutlaka girintili yazılmalıdır.
Genellikle 4 boşluk veya 1 tab kullanılır.
"""

# 2. IF-ELSE YAPISI
# ----------------
print("\n2. if-else Yapısı Örneği:")
yas = 16

if yas >= 18:
    print("Reşitsiniz!")
    print("Ehliyet alabilirsiniz.")
else:
    print("Reşit değilsiniz!")
    print(f"Ehliyet almak için {18 - yas} yıl beklemelisiniz.")

# 3. IF-ELIF-ELSE YAPISI
# ----------------------
print("\n3. if-elif-else Yapısı Örneği:")
not_puani = 85

if not_puani >= 90:
    print("AA - Mükemmel!")
elif not_puani >= 80:
    print("BA - Çok İyi!")
elif not_puani >= 70:
    print("BB - İyi!")
elif not_puani >= 60:
    print("CC - Orta!")
elif not_puani >= 50:
    print("DD - Geçer!")
else:
    print("FF - Kaldınız!")

# 4. İÇ İÇE (NESTED) IF YAPILARI
# ------------------------------
print("\n4. İç İçe if Yapıları Örneği:")
kullanici_adi = "admin"
sifre = "12345"

if kullanici_adi == "admin":
    if sifre == "12345":
        print("Giriş başarılı!")
    else:
        print("Şifre yanlış!")
else:
    print("Kullanıcı adı yanlış!")

# 5. MANTIKSAL OPERATÖRLERLE KOŞULLAR
# ----------------------------------
print("\n5. Mantıksal Operatörlerle Koşullar Örneği:")
yas = 25
mezuniyet = "üniversite"

if yas >= 18 and mezuniyet == "üniversite":
    print("İş başvurusu yapabilirsiniz!")
elif yas >= 18 and mezuniyet != "üniversite":
    print("Sadece bazı pozisyonlara başvurabilirsiniz.")
else:
    print("Başvuru yapamazsınız.")

# 6. IN OPERATÖRÜ İLE KOŞULLAR
# ---------------------------
print("\n6. in Operatörü Örneği:")
meyveler = ["elma", "armut", "muz", "kiraz"]
aranan = "muz"

if aranan in meyveler:
    print(f"{aranan} meyve listesinde var!")
else:
    print(f"{aranan} meyve listesinde yok!")

# 7. KISA IF-ELSE (TERNARY OPERATOR)
# --------------------------------
print("\n7. Kısa if-else Kullanımı Örneği:")
yas = 20
durum = "Reşit" if yas >= 18 else "Reşit değil"
print(f"Durum: {durum}")

"""
ÖZET VE İYİ UYGULAMALAR
-----------------------
1. Kontrol yapıları programın akışını yönlendirir
2. Girintilere (indentation) dikkat edilmelidir
3. Koşullar mantıksal operatörlerle (and, or, not) birleştirilebilir
4. İç içe if yapıları kullanılabilir, ancak çok fazla iç içe kullanmaktan kaçınılmalıdır
5. Kısa if-else yapısı (ternary operator) basit koşullarda kullanılabilir
6. Koşullar açık ve anlaşılır olmalıdır

ALIŞTIRMALAR
-----------
1. Bir sayının pozitif, negatif veya sıfır olduğunu kontrol eden program yazın
2. Kullanıcının girdiği üç sayıdan en büyüğünü bulan program yazın
3. Bir öğrencinin notuna göre harf notu veren program yazın
"""

# Alıştırma 1: Sayı Kontrolü
print("\nAlıştırma 1 - Sayı Kontrolü:")
sayi = -5

if sayi > 0:
    print("Sayı pozitif")
elif sayi < 0:
    print("Sayı negatif")
else:
    print("Sayı sıfır")

# Alıştırma 2: En Büyük Sayı
print("\nAlıştırma 2 - En Büyük Sayı:")
a, b, c = 15, 25, 10

if a >= b and a >= c:
    en_buyuk = a
elif b >= a and b >= c:
    en_buyuk = b
else:
    en_buyuk = c

print(f"En büyük sayı: {en_buyuk}")

# Alıştırma 3: Not Hesaplama
print("\nAlıştırma 3 - Not Hesaplama:")
not_puani = 78

if not_puani >= 90:
    harf_notu = "AA"
elif not_puani >= 85:
    harf_notu = "BA"
elif not_puani >= 80:
    harf_notu = "BB"
elif not_puani >= 75:
    harf_notu = "CB"
elif not_puani >= 70:
    harf_notu = "CC"
elif not_puani >= 65:
    harf_notu = "DC"
elif not_puani >= 60:
    harf_notu = "DD"
else:
    harf_notu = "FF"

print(f"Not: {not_puani} - Harf Notu: {harf_notu}") 