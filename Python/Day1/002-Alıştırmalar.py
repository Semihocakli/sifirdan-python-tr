'''
1.) Bir öğrencinin matematik dersinden aldığı notlar sırasıyla 64, 86 ve 70’tir. Bu öğrencinin not ortalamasını hesaplayınız.

ilk_Ogrenci = float(input("İlk öğrencinin notunu giriniz:"))
ikinci_Ogrenci = float(input("İlk öğrencinin notunu giriniz:"))
ucuncu_Ogrenci = float(input("İlk öğrencinin notunu giriniz:"))

ortalama = (ilk_Ogrenci + ikinci_Ogrenci + ucuncu_Ogrenci) / 3 

print(ortalama)

'''

'''
2.)Kullanıcıdan adını ve yaşını alarak adını yaşı kadar yazdıran programı yazınız.

ad = input("Lutfen adinizi giriniz: ")
yas = int(input("Lutfen yasinizi giriniz: "))

print(ad * yas)

'''

'''
3.) Dairenin alanını ve çevrenisi hesaplayan bir progrm yazınız. Pi değerini ve yarı çap değerini kullanıcıdan alınız.

print("Dairenin Alani ve cevresi icin istenenleri yaziniz\n")
pi = int(input("Lutfen pi'nin degerini giriniz (3,418 civarında alabilirsiniz :)) : "))
r = int(input("Lutfen yaricap degerini giriniz: "))

daire_Alani = pi * r**2
daire_Cevresi = 2 * pi * r

print("Dairenin Alani: ",daire_Alani ,
      "Dairenin Cevresi: ", daire_Cevresi)

'''

'''
4.) Kullanıcıdan doğum tarihini isteyerek ehliyet alma durumunu belirten programı yazınız.
dogum_Tarihi = int(input("Lutfen dogum tarihinizi 'yyyy' olarak giriniz: "))

ehliyet = (2023 - dogum_Tarihi) >= 18 

print("Eger ehliyet alabilecek yaşta iseniz 'True' ifadesini alacaksınız:" , ehliyet)

'''

'''
5.) Kullanıcıdan faiz oranı ve para miktarını öğrenerek, girilen paranın yıllık faizini hesaplayan programı yazınız.

#Aylık Faiz Getirisi = (Anapara / 100) x (Faiz Oranı / 12) x Ay Sayısı 

faiz_Orani = int(input("Lutfen yillik faiz oranini giriniz: "))
para_Miktari = int(input("Lutfen para miktarini giriniz: "))
ay_Sayisi = int(input("Lutfen ay sayisini giriniz: "))

Aylik_Faiz_Getirisi = ((para_Miktari / 100) * (faiz_Orani / 12) * ay_Sayisi )

print("Ana paranin yillik faizi: ", Aylik_Faiz_Getirisi)

'''

'''
6.) Kullanıcıdan alacak olduğunuz veriler ile kullanıcının vücud kitle endeksini hesaplayan programı yazınız.

#VKİ: Agirlik / (boy)*(boy) 
agirlik = float(input("Lutfen kilonuzu 'kg' cinsinden yaziniz: "))
boy = float(input("Lutfen boyunuzu 'cm' cinsinden yaziniz: "))

VKİ = agirlik / (boy)*(boy)

print("Siz",boy ,"cm", agirlik ,"kilosunuz","buna göre vücut kitle endeksiniz:",VKİ )

'''

'''
7.) kullanıcının sizinle adaş olup olmadığını yazdıran programı yazınız.

sizin_adiniz = input("Lutfen isminizi giriniz: ")
benim_adim = "Semih"

print("Eger adaş isek 'True' degil isek 'False' dönecektir ->" , sizin_adiniz == benim_adim)

'''

''' **
8.) Kullanıcıdan not ortalamasını isteyerek teşekkür, takdir alıp alamama durumunu yazdıran programı yazınız.

ortalama = float(input("Lutfen not ortalamanizi giriniz: "))

tebrik_mesaji = (ortalama >= 85) * "Tebrikler Takdir Aldiniz" + (70 <= ortalama < 85) * "Tebrikler Tesekkür Aldiniz"

print(tebrik_mesaji)

'''

'''
9.) Kullanıcıdan otoban uzunluğunu ve geçiş süresini isteyerek hızınız hesaplayınız. daha sonra kullanıcının hız cezası alıp almama durumunu yazdırınız.

otoban_uzunlugu = float(input("Lutfen otoban uzunlugunu (km cinsinden) giriniz: "))
gecis_suresi = float(input("Lutfen gecis suresini (saat cinsinden) giriniz: "))

hiz = otoban_uzunlugu / gecis_suresi

print("Hiziniz:", hiz, "km/saat")

ceza_miktari = (hiz - 120) * 5 * (hiz > 120)

ceza_mesaji = "Hiz sinirini asarak ceza aldin. Ceza miktari: " + str(ceza_miktari) + " TL" * (ceza_miktari > 0)
guvenli_mesaji = "Hiz sinirini asmadiniz. Guvenli seyahatler!" * (ceza_miktari == 0)

print(ceza_mesaji + guvenli_mesaji)

'''

'''
10.) Yevmiyesi 350 TL olan bir işçinin çalışma gün sayısını öğrenerek, yevmiye tutarıı hesaplayan programı yazınız

yevmiye = 350  

calisma_gun_sayisi = int(input("Lutfen calisma gun sayisini giriniz: "))

toplam_odeme = yevmiye * calisma_gun_sayisi

print("Toplam odeme tutari:", toplam_odeme, "TL")

'''
