#https://www.w3schools.com/python/python_ref_string.asp

 # -5 -4 -3 -2 -1
 #  s  e  m  i  h 
 #  0  1  2  3  4

# ad [1 : 4 ] = ad [baslangic : bitis ]
# karakter_dizisi[alınacak_ilk_öğenin_sırası:alınacak_son_öğenin_sırasının_bir_fazlası]


ad = "semih"
pacalama = ad[1:3]
print(pacalama)

print("ad degiskeninin 2. harfini alma 'ad[1]'-> " , ad[1]) # Sonuç : e
print("ad degiskeninin kac harf oldugunu integer seklinde verme 'len(ad)'-> " , len(ad)) # Sonuç : 5 
print("başlangıctan (arası) bitene kadar: 'ad[1:4]'-> ", ad[1:4]) # Sonuç : emi
print("sondan 3' e kadar (3 dahil degil) 'ad[3:]'-> " , ad[3:])  # Sonuç : ih
print("önden 3' e kadar (3 dahil) 'ad[:3]'-> " ,ad[:3])  # Sonuç : sem
print("belirlediğiniz aralıktaki başlangıç karakterinden 2 karakter arayla alma 'ad[1:5:2]' = ",ad[1:5:2]) # Sonuç : ei
# baslangıc : bitis : kaçar arayla alinacagi

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_slice = my_list[::-1]  # Tersine çevrilmiş dilimleme
print(reversed_slice)  # Sonuç: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

soyad = "ocakli"
tam_Ad = ad.upper()[0] + ad.lower()[1:] + " " + soyad.upper()[0] + soyad.lower()[1:6] # Sonuç : Semih Ocakli
"""
print(tam_Ad)

site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"

for isim in site1, site2, site3, site4:
    print("site: ", isim[4:-4])


    isim[4:-4], bu ikisinin birleşimidir: 4. indeksten başlayıp sondan 4 karakter öncesine kadar olan kısmı alır.
    isim[4:] ifadesi, isim stringinin 4. indeksinden itibaren (indeks 0'dan başlar) sonuna kadar olan kısmını alır.
    isim[:-4] ifadesi, isim stringinin başından başlayarak sondan 4 karakter öncesine kadar olan kısmını alır.
    
for i in reversed("Sana Gül Bahçesi Vadetmedim"):
    print(i, end="")

print(sorted("kitap")) # sıralama

for i in enumerate("semih"):
    print(i)

tr_harfler = "şçöğüİı"
a = 0

while a < len(tr_harfler):
    print(tr_harfler[a], sep="\n")
    print(a, "=", tr_harfler[a])
    a += 1
"""

# string methodları
# Replace() -> karakter_dizisi.replace(eski_karakter_dizisi, yeni_karakter_dizisi)
"""
kardiz = "memleket"
kardiz.replace("ket", "KET") # memleKET
print(kardiz.replace("e","")) # mmlkt
print(kardiz.replace("e", "", 1) #mmleket
"""
# Split() -> kelimeleri ayırır
kardiz = "İstanbul Büyükşehir Belediyesi"
kardiz.split() # ['İstanbul', 'Büyükşehir', 'Belediyesi']

kardiz = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin: ")

for i in kardiz.split():
    print(i[0], end="")

# capitalize() -> karakter dizilerinin yalnızca ilk harfini büyütür <-> title()
# swapcase()-> büyük harfleri küçük harfe, küçükleri büyük harfe çevirir
# join() -> birleştirme

kalkış       = input("Kalkış yeri: ")
varış        = input("Varış yeri: ")
isim_soyisim = input("İsim ve soyisim: ")
bilet_sayısı = input("Bilet sayısı: ")

print("""{} noktasından {} noktasına, 14:30 hareket saatli
sefer için {} adına {} adet bilet ayrılmıştır!""".format(kalkış,
                                                         varış,
                                                         isim_soyisim,
                                                         bilet_sayısı))

isim = "Dmitri"
print(f"benim adım {isim} ")

fstring = "f-string"
f"{{ {fstring}: f'{{ifade}}' şeklinde kullanılır. }}"

"""
istihza = "Python Istihza"

f"{istihza:^30}"   # "istihza".center(30)
'        Python Istihza        '

f"{istihza:-^30}"  # "istihza".center(30, '-')
'--------Python Istihza--------'

f"{istihza:30}"    # "istihza".ljust(30)
'Python Istihza                '

f"{istihza:>30}"   # "istihza".just(30)
'                Python Istihza'

f"{istihza:>030}"  # "istihza".zfill(30)
'0000000000000000Python Istihza'
"""