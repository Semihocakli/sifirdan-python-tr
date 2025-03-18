'''
class Ogrenci:
    isim = "Mehmet"
    soyisim = "Tek"
    yas = 29
    not_ort = 85

Ogrenci.isim
print(Ogrenci.yas)

print(type("mehmet"))
print(type(Ogrenci.isim))
print(type(Ogrenci))

ogr1 = Ogrenci()
ogr2 = Ogrenci()
ogr1.isim = "semih"
ogr2.yas = 35
print(ogr1.isim)
print(ogr2.isim)

class Araba:
    marka = ""
    renk = ""
    plaka =""

araba1 = Araba()
araba1.marka = "FORD"
araba1.renk = "Siyah"
araba1.plaka = "34 P 148"

araba2 = Araba()
araba2.marka ="BMW"
araba2.renk ="Beyaz"
araba2.plaka ="04 GH 48"

print("-------ARABA 1------")
print("Marka: {} \nRenk :{}\nPlaka :{}".format(araba1.marka,araba1.renk,araba1.plaka))

print("-------ARABA 2------")
print("Marka: {} \nRenk :{}\nPlaka :{}".format(araba2.marka,araba2.renk,araba2.plaka))

print("*" * 20)


class Araba:
    marka = ""
    renk = ""
    plaka =""
    hiz = 0

    def hizArttir(self):
        self.hiz +=10
        return self.hiz

araba = Araba()
araba.marka ="FORD"
araba.renk ="Siyah"
araba.plaka ="34 P 148"

print("-------ARABA ------")
print("Marka: {} \nRenk :{}\nPlaka :{}".format(araba.marka,araba.renk,araba.plaka))
araba.hizArttir()
print("Hız :",araba.hiz)


class Ogrenci:
    
    def __init__(self):
        self.selamla = "selam"
        self.ad = "Semih"
        self.soyad = ""

ogr1 = Ogrenci()
print(ogr1.ad)
print(ogr1.selamla)


class Ogrenci:

    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad

    def tam_isim(self):
        tam_isim = self.ad + " " + self.soyad
        return tam_isim
    
ogr1 = Ogrenci(ad="Semih", soyad="Ocakli")
print(ogr1.tam_isim())


class calisan:
    zam_oranı = 1.05
    per_say = 0

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
        calisan.per_say = calisan.per_say + 1

    def tamad(self):
        return "adı : {}  soyadı : {}  maaşi: {} e-postasi: {}".format(self.ad,self.soyad,self.maas,self.eposta)
    
    def arttir(self):
        # self.maas = (self.maas*1.05)
        # self.maas = (self.maas * calisan.zam_oranı)
        self.maas = (self.maas * self.zam_oranı)

print("calisan personel sayisi: " ,calisan.per_say)
personel1 = calisan(ad="Semih", soyad="ocakli", maas= 18000)
print(personel1.tamad())
print("calisan personel sayisi: " ,calisan.per_say)

'''
class Calisan:

    zam_oranı = 1.05
    per_say = 0

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
        Calisan.per_say = Calisan.per_say + 1
    def tamad(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)

    def arttir(self):
        # self.maas = (self.maas*1.05)
        # self.maas = (self.maas * calisan.zam_oranı)
        self.maas = (self.maas * self.zam_oranı)

    @classmethod
    def zam_orani_degis(cls,yeni_oran):
        cls.zam_oranı = yeni_oran

    @classmethod
    def ypersonel(cls,pbilgisi):
        ad, soyad, maas = pbilgisi.split("-")
        return cls(ad,soyad,maas)

    @staticmethod
    def tel_no(telefon):
        return telefon.split(" ")
    
personel1 = Calisan(ad="Semih", soyad="ocakli", maas= 18000) 
personel1.arttir()
print(personel1.maas)
print(personel1.zam_oranı)
Calisan.zam_orani_degis(1.2)
print(personel1.zam_oranı)

mpersonel1 = "sonay-karaslan-50000"

yeni_personel = Calisan.ypersonel(mpersonel1)

print(yeni_personel.ad)