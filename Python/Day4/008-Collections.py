#https://derslik.kerteriz.net/python-dersleri/temel-dersler/python-diziler/python-listeler

''' 
    --- LİST ----

liste = [ "ankara" , 'izmir' , '77' , 77 ]
listele = list(("Ankara", 'şzmşr'))

print(listele[0])
print(liste)

#         0   1   2   3   4   5   6
liste = ["a","b","c","d","e","f","g"]
#        -7  -6  -5  -4  -3  -2  -1

yeniliste = liste[2:5]
yepyeniliste= liste[-5:-1]

# Bu şekilde yeni liste oluştururken [x:y] ifadesinde x dahil, y dahil değildir.
 
print(yeniliste) 
print(yepyeniliste) 

# Listeler ile çalışırken listenin sonuna rahatlıkla yeni bir eleman ekleyebilirsiniz. Bunun için append() fonksiyonu kullanırız.
meyveler = ["kivi","çilek"]

meyveler.append("muz")

print(meyveler)

# Eğer listenin sonuna değilde belirlediğiniz indeks numarasına eleman eklemek istiyorsanız insert() fonksiyonunu kullanmalısınız.
meyveler = ["kivi","çilek"]

meyveler.insert(1,"muz")

print(meyveler)

# Listeden çıkarmak istediğiniz elemanı belirterek remove() fonksiyonunu kullanmaktır.
meyveler = ["kivi","çilek","muz","armut"]

meyveler.remove("çilek")

print(meyveler)

# 
# 1'den 10'a kadar olan sayıları içeren bir liste oluşturmak için range() kullanma
sayilar = list(range(1, 11))

# Elde edilen liste
print(sayilar)

'''
''' 
    ----TUPLES---
# sıralanabilen , indekslenebilen, çoğul elemana izin veren ama değiştirilemeyen bir veri tipidir. Yuvarlak parantezlerle ( ) oluşturulur.

t = 'x', 'y' , 'z'
print(t)
t = ("x" , "y" , "z")

print(type(t))

# Bir tuple yeni bir eleman ekleyemezsiniz.Bir tuple eleman çıkaramazsınız.

'''

''' 
    ---SETS---
    
#  sıralanamayan , değiştirilemeyen, indekslenemeyen ve çoğul elemana izin vermeyen bir veri tipidir. Süslü parantezlerle { } oluşturulur.

    '''

''' 
DICT(SOZLUK)
#değiştirilebilen , indekslenebilen, çoğul elemana izin veren ama sıralanamayan  bir veri tipidir. Süslü parantezlerle { } oluşturulur.
'''
sozluk = {
         "marka" : "BMW",
         "model" : "i8",
         "yil"   : 2019
         }
         
sozluk = {
         "ulke" : "Türkiye",
         "sehir" : "Ankara",
         "ilce"   : "Yenimahalle"
         }


for x in sozluk:
    print("Anahtar: " + x + " -- " + "Değer: " + sozluk[x])