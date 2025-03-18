''' 
def hatirla_Sevgili():
    print("O mesut geceyi")
    print("Çamların altında")
    print("Verdigin o buseyi")
hatirla_Sevgili()
'''
'''

def topla(a=4, b=5):
    c = int(input("sayi gir: "))
    d = int(input("sayi gir: "))
    return a + b + c + d

sonuc = topla()

print(sonuc)
'''
'''

def daire(pi,r):
    alan = pi * (r**2)
    return alan
print(daire(pi=3.14, r=4))
'''
'''

def sayiyazdir(*sayilar):
    sayilar = list(sayilar)  # Tuple'ı listeye çeviriyoruz
    print(*sayilar)
    for sayi in sayilar:
        print(sayi, end="")

sayiyazdir(1, 2, 3, 45)  # Fonksiyonu doğru şekilde çağırıyoruz
'''
'''

def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)

sayi = int(input("Lutfen bir sayi giriniz: "))
sonuc = faktoriyel(sayi)
print(f"{sayi} faktoriyel = {sonuc}")

'''
'''

def o_listesi(liste):
    if not liste:  
        return
    else:
        print(liste[0])  # Listenin ilk öğesini yazdır
        o_listesi(liste[1:])  # Listenin geri kalanını işlemek üzere fonksiyonu tekrar çağır

o_listesi(["ali", "veli", "can"])

'''
'''
from math import sqrt

def asal(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    kok = round(sqrt(n)) + 1
    for deneme in range(2, kok):
        if n % deneme == 0:
            return False
    return True

def main():
    en_buyuk = int(input("Asal sayilari hangi degere kadar gösterelim: "))
    for deger in range(2, en_buyuk + 1):
        if asal(deger):
            print(deger)

main()
'''
'''

import random
import os


def cikis():
    print("Çıkış Yapıldı - Oyun Bitti")
    exit()


def dosya_kontrol(dosya):
    if not (os.path.exists(dosya_adi)):
        dosya = open(dosya_adi, "x")
        dosya.close()


def oyun(dosya_adi):
    dosya = open(dosya_adi, "a")
    rastgele = random.randrange(1, 100)
    dosya.write(str(rastgele) + "+")
    tahminSayisi = 10
    taban = 0
    tavan = 100
    while tahminSayisi >= 1:
        tahmin = int(input("Bir sayı giriniz"))
        dosya.write(str(tahmin) + ",")
        if tahmin == rastgele:
            dosya.write("+kazandiniz" + "\n")
            print("Tebrikler")
            break
        elif tahmin > rastgele:
            print("daha küçük giriniz")
            tavan = tahmin
        elif tahmin < rastgele:
            print("daha büyük giriniz")
            taban = tahmin
        tahminSayisi -= 1
        print("kalan hakkınız", tahminSayisi)
        if tahmin == 0:
            dosya.write("kaybettiniz" + "\n")
            dosya.close()


def istatistik(dosya_adi):
    dosya = open(dosya_adi, "r")
    print(dosya.readlines())
    dosya.close()


while True:
    dosya_adi = "oyun.txt"
    dosya_kontrol(dosya_adi)
    cevap = int(input("Oyun için :1 \n İstatistik için : 2\t Çıkış için: 3\t"))
    if cevap == 3:
        cikis()
    elif cevap == 1:
        oyun(dosya_adi)
    elif cevap == 2:
        istatistik(dosya_adi)
'''

menu = {
    "Ana Yemekler": ["Köfte", "Kebap", "Tavuk"],
    "Ara Sıcaklar": ["Çiğ Köfte", "Midye Dolma", "Sigara Böreği"],
    "İçecekler": ["Su", "Kola", "Çay"]
}
def menu_goster():
    print("----- MENÜ -----")
    kategori_index = 1
    for kategori in menu:
        print(f"\n{kategori}:")
        yemekler = menu[kategori]
        yemek_index = 1
        for yemek in yemekler:
            print(f"{yemek_index}. {yemek}")
            yemek_index += 1
        kategori_index += 1
    print("----------------")

def secenekleri_goster():
    print("1. Menüyü Göster")
    print("2. Çıkış")

def main():
    while True:
        secenekleri_goster()
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            menu_goster()
        elif secim == "2":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

