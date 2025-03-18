'''
1.) Kullanıcıya memleketini sorarak hemşeri olup olmadığınızı yazdıran programı yazınız.

b_memleket = "İzmir"
memleket = input("Memleketin neresi hemşerim ? ")

if memleket == b_memleket :
    print("HEMŞERİMMM")
else:
    print("Degiliz")
'''

'''
2.) Kullanıcıdan iki sayı isteyerek büyük olanı ve küçük olanı saırasıyla ekrana yazdıran uygulamayı yazınız.

sayi1 = int(input("Lutfen sayi1 degerini giriniz:"))
sayi2 = int(input("Lutfen sayi2 degerini giriniz:"))

if sayi1 > sayi2:
    print("Sayi1:", sayi1, "> Sayi2" , sayi2)
elif sayi1 == sayi2:
    print("sayi1 ve sayi2 degerleri esittir")
else:
  print("Sayi1:", sayi1, "< Sayi2:", sayi2)

'''

'''
3.) Kullanıcıdan 3 adet sayı isteyerek sayıları büyükten küçüğe sırayla yazdırınız.

sayi1 = float(input("Lütfen birinci sayıyı giriniz: "))
sayi2 = float(input("Lütfen ikinci sayıyı giriniz: "))
sayi3 = float(input("Lütfen üçüncü sayıyı giriniz: "))


if sayi1 >= sayi2 and sayi1 >= sayi3:
    en_buyuk = sayi1
    if sayi2 >= sayi3:
        orta = sayi2
        en_kucuk = sayi3
    else:
        orta = sayi3
        en_kucuk = sayi2
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    en_buyuk = sayi2
    if sayi1 >= sayi3:
        orta = sayi1
        en_kucuk = sayi3
    else:
        orta = sayi3
        en_kucuk = sayi1
else:
    en_buyuk = sayi3
    if sayi1 >= sayi2:
        orta = sayi1
        en_kucuk = sayi2
    else:
        orta = sayi2
        en_kucuk = sayi1

print("Sayılar büyükten küçüğe sırayla:", en_buyuk, orta, en_kucuk)

'''

'''
4.) küşüye ehliyet için gerekli yaş ve eğitim sorularını sararak ehliyet alma durumunu yazdırınız (eğitim için ilkenaz ilköğretim mezunu olması gerekmektedir)

print("Ehliyet belgesi almanız için gerekli olan soruları cevaplayınız!")

yas = int(input("Lütfen yaşınızı giriniz: "))
egitim = input("Lütfen eğitim durumunuzu giriniz (ilkenaz ilkogretim kurumu için 'evet', değilse 'hayir'): ")

if yas >= 18 and egitim == "evet":
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsınız.")

'''

'''
5.) Bir turnava düşünerek gerekli koşulları belirleyiniz. en az iki koşul olmak üzere kullanıcının turnuvaya katılıp katılmayacağı bilginizi veren programı yazınız.

print("Turnuvaya katılma durumunuzu kontrol eden programa hoş geldiniz!")

yas = int(input("Lütfen yaşınızı giriniz: "))
kayit_durumu = input("Turnuvaya kayıt yaptırdınız mı? (evet/hayır): ")


if yas >= 18:
    print("Yaşınız uygun.")

    if kayit_durumu == "evet":
        print("Turnuvaya katılabilirsiniz.")
    else:
        print("Turnuvaya katılamazsınız, çünkü kayıt yaptırmadınız.")
else:
    print("Yaşınız uygun değil, turnuvaya katılamazsınız.")

'''

'''
6.) bir menü sipariş kontol sistemi yazınız. müşterinin menüsünün doğru olup olmadığını kontrol ediniz.(bir yiyecek ve içecek olmalı)

istek = input("Lütfen almak istediğiniz menuyu giriniz (1, 2, 3, 4): ")

menu1 = "mantı ve kola" 
menu2 = "pizza ve kola"
menu3 = "zurna ve ayran"
menu4 = "tavuk ve ayran"

if istek == "1":
    print("sectiginiz menu : " ,menu1)
elif istek == "2":
    print("sectiginiz menu : " ,menu2)
elif istek == "3":
    print("sectiginiz menu : " ,menu3)
elif istek == "4":
    print("sectiginiz menu : " ,menu4)
else:
    print("Geçersiz bir seçim yaptınız.")

'''

'''
7.) Hergün bir farklı bir mahalleye gidecek olan pazarlama elemanının, haftanın hangi gününde hangi mahallede olacak olduğunu söyleyen bir program yazınız.(elifli yapı)

gün = input("Pazarlama elamanının calistigi haftanın bir gününü giriniz (pzt, salı, carsmba, persmbe, cuma, cmt, pazar): ")

if gün == "pzt":
    print("pazartesi günü değirmenderede")
elif gün == "salı":
    print("Salı günü konakta")
elif gün == "carsmba":
    print("carsamba günü karsıyakada")
elif gün == "persembe":
    print("persembe günü menemende")
elif gün == "cuma":
    print("cuma günü aliagada")
elif gün == "cmt":
    print("cumartesi günü altınderede")
elif gün == "pazar":
    print("pazar günü bornovada")
'''

'''
8.) Kullanıcıdan üç adet oratalama isteyerek ders gerçeme durumunu yazdıran programı yazınız.
9.) Yukarıda ki soruya devam drumunu da ekleyerek geçme kalma durumunu belirtiniz.

ortalama1 = int(input("Lutfen bir bölüm ortalaması giriniz: "))
ortalama2 = int(input("Lutfen bir bölüm ortalaması giriniz: "))
ortalama3 = int(input("Lutfen bir bölüm ortalaması giriniz: "))

if (ortalama1+ ortalama2 + ortalama3) / 3 >= 70:
    print("Ortalamanız yeterli")
    devamsizlik = int(input("Devamsizlik durumunu giriniz "))
    if devamsizlik < 5:
        print("Devamsizliginiz bulunmamaktadir" + " Bölümü başarıyla bitirdiniz")
    else:
        print("Devamsizliktan kaldiniz")
else:
    print("Ortalamaniz yetmedi kaldiniz")
'''

''' **
10.) Kullanıcı adı ve şifre isteyerek doğru bilgileri girmesi halinde kullanıcıya hoşgeldin mesajı veren uygulamayı yazınız.

id = "semihocakli35"
password = "ASDAF35"

kullanici_id = input("Lutfen kullanici ismini giriniz: ")
kullanici_password = input("Lutfen parolayi giriniz: ")

if id == kullanici_id and password == kullanici_password:
    print("WELCOME!")
elif id == kullanici_id and password != kullanici_password:
    print("Hatalı Şifre girdiniz! ")
else:
    print("Hatali giriş yaptiniz!")
'''

'''
11.) Kullanıcıya sevdiği programlama dilini sorarak, o programlama dilini geliştiren kişi(leri)n ismini yazıran programı yazınız. 4 adet yeterli

print("En sevdiğiniz programlama dili nedir ? ")

python = "Guido van Rossum"
javascript = "Brendan Eich"
java = "James Gosling"
c = "Dennis Ritchie"

dil = input("Lutfen en sevdiginiz yazilim dilini yaziniz (python,javascript,java,c): ")

if dil == "python":
    print("sectiginiz dili gelistiren kisi: " ,python)
elif dil == "javascript":
    print("sectiginiz dili gelistiren kisi: " ,javascript)
elif dil == "java":
    print("sectiginiz dili gelistiren kisi: " ,java)
elif dil == "c":
    print("sectiginiz dili gelistiren kisi: " ,c)

'''

'''
12.) Kullanıcıya seçtiği menüye göre fiyat bilgisi veren restoran uygulamasını yazınız.

print("Restoran Menüsü")
print("1. Mantı ve Kola - 20 TL")
print("2. Pizza ve Kola - 25 TL")
print("3. Zurna ve Ayran - 15 TL")
print("4. Tavuk ve Ayran - 18 TL")

secim = input("Lütfen bir menü numarası seçiniz (1, 2, 3, 4): ")

fiyat = 0

if secim == "1":
    fiyat = 20.0
    yemek = "Mantı ve Kola"
elif secim == "2":
    fiyat = 25.0
    yemek = "Pizza ve Kola"
elif secim == "3":
    fiyat = 15.0
    yemek = "Zurna ve Ayran"
elif secim == "4":
    fiyat = 18.0
    yemek = "Tavuk ve Ayran"
else:
    print("Geçersiz bir menü numarası girdiniz.")

if fiyat > 0:
    print(f"Seçtiğiniz menü olan {yemek} fiyatı: {fiyat:} TL")

'''

dogruSifre = "1905"

sifre = int(input("Lütfen şifreyi giriniz: "))


binlerBasamagi = sifre // 1000
yuzlerBasamagi = (sifre % 1000) // 100
onlarBasamagi = (sifre % 100) // 10
birlerBasamagi = sifre % 10
    
dogruBinlerBasamagi = int(dogruSifre) // 1000
dogruYuzlerBasamagi = (int(dogruSifre) % 1000) // 100
dogruOnlarBasamagi = (int(dogruSifre) % 100) // 10
dogruBirlerBasamagi = int(dogruSifre) % 10

if binlerBasamagi == dogruBinlerBasamagi:
    print(dogruBinlerBasamagi, end="")
else:
    print("*", end="")

if yuzlerBasamagi == dogruYuzlerBasamagi:
    print(dogruYuzlerBasamagi, end="")
else:
    print("*", end="")

if onlarBasamagi == dogruOnlarBasamagi:
    print(dogruOnlarBasamagi, end="")
else:
    print("*", end="")

if birlerBasamagi == dogruBirlerBasamagi:
    print(dogruBirlerBasamagi, end="")
else:
    print("*", end="")

if sifre == int(dogruSifre):
    print(" Sifreyi doğru girdiniz!")
else:
    print(" Sifreyi hatalı girdiniz!")

