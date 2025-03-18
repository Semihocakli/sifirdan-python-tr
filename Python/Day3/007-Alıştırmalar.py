'''
1.) 1-30 arasındaki tek sayıları yazdıran programı yazınız

for i in range(1, 31, 2):
    print(i)

'''
'''
2.) Girilen 10 Sayının Toplamını ve ortalamasını Bulan programı yazınız.

toplam = 0
ortalama = 0
for a in range(1,11):
    sayilar = int(input("Lutfen sayilari giriniz: "))
    toplam = toplam + sayilar
    ortalama = int(ortalama + toplam) // 10 

print(toplam)
print(ortalama)
    
'''
'''
3.) Python 50’den 20(dahil ise)’ye kadar olan sayıları 3’er azaltarak ile ekrana yazdırınız.

for a in range(50, 19, -3):
    print(a)

'''
''' **
4.) Girilen 20 sayıdan Tek ve Çift Sayıların Ortalamasını Hesaplattırarak ekrana yazdıran uygulamayı yazınız.

toplam_tek = 0
toplam_cift = 0
tek_sayi_adedi = 0
cift_sayi_adedi = 0

for _ in range(20):
    sayi = int(input("Lütfen bir sayı giriniz: "))
    if sayi % 2 == 0:
        toplam_cift += sayi
        cift_sayi_adedi += 1
    else:
        toplam_tek += sayi
        tek_sayi_adedi += 1

if cift_sayi_adedi > 0:
    ortalama_cift = toplam_cift / cift_sayi_adedi
    print("Çift sayıların ortalaması:", ortalama_cift)
else:
    print("Çift sayı girilmedi.")

if tek_sayi_adedi > 0:
    ortalama_tek = toplam_tek / tek_sayi_adedi
    print("Tek sayıların ortalaması:", ortalama_tek)
else:
    print("Tek sayı girilmedi.")

'''
'''
5.) Python ile iç içe For Döngüsü kullanarak 1′ den 10′ akadar çarpım tablosu oluşturunuz. (Yanyana çıktı veren versiyonunuda deneyiniz)
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")  
    print()  
'''

'''
6.) Python ile iç içe while kullanarak 1′ den 10′ akadar çarpım tablosu oluşturunuz. (Yanyana çıktı veren versiyonunuda deneyiniz)

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(i * j, end="\t")
        j += 1
    print()
    i += 1
'''

''' ** 
7.) Kullanıcıdan 2 kez aynı parolayı girmesini isteyerek, iki defa aynı parola girildiğinde giriş yapan farklı girildiğinde uyaran kodları oluşturun?

parola1 = int(input("Lutfen parolayi giriniz: "))
parola2 = int(input("Lutfen ayni parolayi giriniz: "))

while parola1 != parola2:
        print("Girdiğiniz parolalar eşleşmiyor. Tekrar deneyin.")
        parola1 = input("Lütfen parolanızı girin: ")
        parola2 = input("Lütfen parolanızı tekrar girin: ")

print("Parolalar eşleşti. Giriş başarılı!")

'''
'''
8.) Python 100'e kadar 3'e ve 5'e Tam Bölünen Sayıları Listeleyen Örnek yazınız

print("Listelenmiş Hali: ")
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        for a in range(1):
            print(i, end="\t")

'''
'''
9.) "*" kullanarak 4*4 bir kare olşturunuz.

i = 0
while i < 4:
    kare = ""
    j = 0
    while j < 4:
        kare += "*"
        j += 1
    print(kare)
    i += 1

'''
'''
10.) "*" kullanarak kullanıcının belirlediği ölçülerde bir dikdörtgen oluşturunuz.

satir = int(input("Lütfen satır sayısını giriniz: "))
sutun = int(input("Lütfen sütun sayısını giriniz: "))

for i in range(satir):
    for j in range(sutun):
        print("*", end="")
    print()  

'''
'''
11.) Break deyiminin kullanımı görmek açısından 1'den 100' e kadar sayıları ekrana yazdırırken, her sayıyı kontrol edelim ve eğer sayı 35 ise döngüden çıkalım

for sayi in range(1, 101):
    print(sayi)
    if sayi == 35:
        print("Sayı 35 olduğu için döngüden çıkılıyor.")
        break
        
'''
'''
12.) Şimdi kullanıcıya bir sayı girmesini isteyelim ve break komutu kullanarak 1den kullanıcının girdiği sayıya kadar olan sayıları ekrana yazdıralım.

sayi = int(input("Lutfen bir sayi giriniz: "))
for i in range(1, 101):
    print(i)
    if i == sayi:
        break

'''
'''
13.) Birlikte sayı bulmaca yapalım. sayimiz isimli bir değişken tanımlayıp, 1 ile 100 arasında istediğimiz bir sayıyı o değişkene atayalım. Ve kullanıcıya bir sayı girmesini isteyelim. Kullanıcı tuttuğumuz sayıyı yanlış girdiğinde "Yanlış, Bir kez daha dene!" mesajını ekrana yazdıralım. Doğru sayıyı girdiğinde ise ekrana "Tebrikler Kazandınız" şeklinde bir uyarı mesajı yazdıralım.

hedef_sayi = int(input("1 ile 100 arasında bir hedef sayı girin: "))

while True:
    tahmin = int(input("Tahmininizi girin: "))
    if tahmin == hedef_sayi:
        print("Tebrikler! Kazandınız.")
        break  
    else:
        print("Yanlış, Bir kez daha dene!")
'''
'''
14.) Python 100'e kadar 3'e ve 5'e Tam Bölünen Sayılar harici sayıları Listeleyen Örnek yazınız

print("Listelenmiş Hali: ")
for i in range(1,101):
    if i % 3 != 0 and i % 5 != 0:
        for a in range(1):
            print(i, end="\t")

'''
''' **
15.) Kullanıcıdan 10 sayı girmesini ve girilen sayıların faktöriyel değerlerini toplamasını isteyinizisteyiniz. negatif bir sayı girildiğinde sayı isteme işlemini bitirerek girilen toplam sayı adetini ve elde edilen toplamı kullanıcıya yazdırırken, 7 ve katları sayılar girildiğinde gerekli hesaplamaları yapmayarak devam eden uygulamayı yazınız.

toplam = 0
sayac = 0
carpim = 1

while sayac < 10:
    sayi = int(input("Lütfen bir sayı girin: "))
    
    if sayi < 0:
        break  
    
    if sayi % 7 == 0:
        print("Bu sayıyı hesaplamaya katmıyoruz.")
        continue 
    
    for i in range(1, sayi + 1):
        carpim *= i  
        
    toplam += carpim  
    sayac += 1  

print("Toplam sayı adeti:", sayac)
print("Elde edilen toplam:", toplam)

'''
'''
16.) Girilen iki sayının ebob ve ekok değerlerini bulup yazdıran programı yazınız.

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

ebob = 1
bolen = 2
while bolen <= sayi1 and bolen <= sayi2:
    if sayi1 % bolen == 0 and sayi2 % bolen == 0:
        ebob = bolen
    bolen += 1

ekok = (sayi1 * sayi2) // ebob

print(f"Girilen sayıların EBOB değeri: {ebob}")
print(f"Girilen sayıların EKOK değeri: {ekok}")

'''
'''
17.) Python ile girilen sayının basamak sayısını bulan kodu yazınız

sayi = int(input("Bir sayı girin: "))
basamak_sayisi = len(str(abs(sayi)))

print(f"Girilen sayının basamak sayısı: {basamak_sayisi}")

'''
'''
18.) (43) + (03) + (73) = 407 yapmaktadır. Yani bu demektir ki 407 sayısı Armstrong bir sayıdır. Şimdi bunu Python ile kodlayınız.
'''
'''
 :/
'''
