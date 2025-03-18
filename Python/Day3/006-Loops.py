'''
for değişken_adı in değişken:
    yapılacak_işlem

for dd in range(1,11):
    print( dd,"." ,"Sallakazan")

'''

'''
baslangiç = int(input("Baslangic degeri giriniz")) 
bitis = int(input("Baslangic bitis giriniz")) 
artis = int(input("Baslangic artis giriniz"))
for abv in range(baslangiç , bitis , artis):
     print(abv)

ad = input("Lutfen adinizi girer misiniz: ")
yas = int(input("Lutfen yasinizi girer misiniz: "))
for aga in range(yas):
    print(ad)

'''
'''
pizza = int(input("Kaç dilim pizza yersiniz: "))

for a in range(pizza):
    print(str(a+1) + "." + " dilim pizzanız")


n = int(input("Lutfen bir deger giriniz: "))
toplam = 0
for bb in range(n):
    toplam = toplam + bb
    print(str(bb+1) + "." , toplam)

n = int(input("Lutfen bir deger giriniz: "))
fak = 1
for bb in range(n):
    fak = fak * (bb+1)
    print(str(bb+1) + "!  = " , fak)

isim = "SemihOcakli"

for harf in isim:
    print(harf)

a = 0 
while a < 10:
    print(a)
    a+=1
'''
'''
carpim = 1
sayi = int(input("Bir sayı giriniz: "))
sayac = 0

while sayac < 10:
    if sayi == 0:
        print("Girdiğiniz sayıların çarpımı:", carpim)
        break
    
    carpim *= sayi
    sayac += 1
    sayi = int(input("Bir sayı giriniz: "))

'''

for dd in range(1,11,2):
    print( dd,"." ,"Sallakazan")

print("my name is")

for i in range(5):
    print('Semih ('+ str(i) +')')


# for 'un farklı kullanımları: 
"""

metin = "SemihOcakli kütahya sağlık bilimleri üniversitesinde okuyor"

harf = input("Lutfen bir harf giriniz: ")

sayac = 0

for kelime in metin:
    if harf == kelime:
        sayac += 1

print("Girdiğiniz harf metinde", sayac, "kadar bulunmaktadır.")
"""

hakkinda = "SemihOcakli kütahya sağlık bilimleri üniversitesinde okuyor"
sayi = 0
harf = input("Sorgulamak istediğiniz harf: ")

for karakter_dizisi in hakkinda:
    print(repr(karakter_dizisi))
    # for karakter in karakter_dizisi:
    #     # print(karakter)
    #     if harf == karakter:
    #         sayi += 1
print(sayi)
