'''
1.) bilgisayarın tuttuğu rastgele bir sayıyı bulmaya çalışan bir uygulama yazınız.

import random

tutulan_sayi = random.randint(1, 50)

while True:
    sayi = int(input("Tahmininizi girin (1-50 arası): "))

    if sayi == tutulan_sayi:
        print(f"Tebrikler! Tutulan sayıyı {sayi} olarak doğru tahmin ettiniz.")
        break
    elif sayi < 1 or sayi > 50:
        print("Geçersiz tahmin! Lütfen 1 ile 50 arasında bir sayı girin.")
    elif sayi < tutulan_sayi:
        print("Daha yüksek bir sayı tahmin edin.")
    else:
        print("Daha düşük bir sayı tahmin edin.")

'''
    

'''
2.) sizin tuttuğunuz sayıyı bulmaya çalışan bir uygulama yazınız. (yönlendirmeler olmalı daha büyük ve daha küçük şeklinde)
import random

print("Bir sayı tuttum. Şimdi bu sayıyı tahmin etmeye çalışın.")

tutulan_sayi = random.randint(1, 100)

tahmin_sayisi = 0 

while True:
    tahmin = int(input("Tahmininizi girin (1-100 arası): "))
    tahmin_sayisi += 1

    if tahmin < tutulan_sayi:
        print("Daha büyük bir sayı tahmin edin.")
    elif tahmin > tutulan_sayi:
        print("Daha küçük bir sayı tahmin edin.")
    else:
        print(f"Tebrikler! {tutulan_sayi} sayısını {tahmin_sayisi}. tahminde buldunuz!")
        break

'''
'''
3.) bir sayısal loto programı yazınız.
'''
'''
4.) Sinüs teoremi kullanarak alan hesabı yapan bir uygulama yazınız.

import math

# Kullanıcıdan üçgenin kenarlarını ve açıyı girmesini isteyin
a = float(input("Üçgenin birinci kenarını (a) girin: "))
b = float(input("Üçgenin ikinci kenarını (b) girin: "))
C_degrees = float(input("Bu iki kenar arasındaki açıyı (derece cinsinden) girin: "))

# Dereceyi radyana çevirin
C_radians = math.radians(C_degrees)

# Sinüs teoremini kullanarak üçgenin alanını hesaplayın
alan = 0.5 * a * b * math.sin(C_radians)

# Sonucu ekrana yazdırın
print(f"Üçgenin alanı: {alan}")

'''
'''
5.) kişiden doğum tarihini isteyerek kaç, kaç hafta ve kaç gündür hayatta olduğunu hesaplayan programı yazınız.

from datetime import datetime

# Doğum tarihini kullanıcıdan alın
dogum_tarihi = input("Lütfen doğum tarihinizi (GG.AA.YYYY) girin: ")

# Doğum tarihini datetime nesnesine çevirin
dogum_tarihi = datetime.strptime(dogum_tarihi, "%d.%m.%Y")

# Şu anki tarihi alın
bugun = datetime.now()

# İki tarih arasındaki farkı hesaplayın
fark = bugun - dogum_tarihi

# Farkı hafta ve gün olarak hesaplayın
hafta = fark.days // 7
gun = fark.days % 7

# Sonucu ekrana yazdırın
print(f"Siz {hafta} hafta ve {gun} gün hayattasınız.")

'''
'''
6.) bir test sınavı uygulaması yazarak 1 dakikada bir soru soran ve cevap kontrolü yaparak test sonucunu hesaplayan bir uygulama yazınız.
import time

# Soru ve cevaplar
sorular = ["2 + 2 = ?", "Başkentin hangi şehir?", "En büyük gezegen nedir?"]
cevaplar = ["4", "Ankara", "Jüpiter"]

# Test süresi (saniye cinsinden)
test_suresi = 60  # 1 dakika

# Başlangıç zamanı
baslangic_zamani = time.time()

# Test sınavı
dogru_cevaplar = 0
soru_sayisi = len(sorular)

for i in range(soru_sayisi):
    soru = sorular[i]
    cevap = input(f"Soru {i + 1}: {soru} Cevap: ")
    
    if cevap == cevaplar[i]:
        dogru_cevaplar += 1

    # Zamanı kontrol et ve test süresini doldurmuşsa çık
    simdiki_zaman = time.time()
    gecen_sure = simdiki_zaman - baslangic_zamani
    if gecen_sure >= test_suresi:
        print("Zaman doldu! Testi tamamlayamadınız.")
        break

# Sonuçları göster
print(f"\nTest sonucunuz: {dogru_cevaplar}/{soru_sayisi} doğru cevap")

'''
'''
7.) sezar şifreleme yöntemini öğrenerek bir metni sezar şifreleme yöntemi ile şifreleyiniz.
'''
'''
8.) round kütüphanesini kullanarak çeşitli sayı yuvarlama işlemlerini yapınız.

sayi = 5.8
yaklasik_sayi = round(sayi)  # En yakın tam sayıya yuvarla
print(yaklasik_sayi)  # Sonuç: 6

'''
'''
9.) bir alan hesaplayıcı yaparak, çeşitli çok hesapları yapınız. yapacak olduğunuz hesaplamaları bir dosyaya kaydettirerek, sonrasında kullanıcıya dosyadan okutarak istatistiksel olarak bilgilendirme yapınız.
'''
'''
10.) kullanıcıdan bir dosya adı isteyerek aradığınız dizinde o dosyanın olup olmadığı bilgisini kullanıcıya veren uygulamayı yazınız.

import os

# Kullanıcıdan dosya adını alın
dosya_adı = input("Dosya adını girin: ")

# Dosyanın bulunması gereken dizini belirtin (örneğin: C:/Users/Kullanıcı/Belgeler)
# Kendi sistem yolunuzu buraya girin
dizin = "C:/Users/Kullanıcı/Belgeler"  # Değiştirin

# Dosyanın tam yolu oluşturun
dosya_yolu = os.path.join(dizin, dosya_adı)

# Dosyanın varlığını kontrol edin
if os.path.exists(dosya_yolu):
    print(f"{dosya_adı} dosyası {dizin} dizininde bulunuyor.")
else:
    print(f"{dosya_adı} dosyası {dizin} dizininde bulunmuyor.")

'''