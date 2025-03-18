a = [1,2,3]

print(a)

"""
spam = ["a","b","c","d"]
spam[0] = "a" , spam[1] = "b" , spam[2] = "c" , spam[3] = "d"
"""
"""
----------- veri[start:stop:step] --------------

start: Dilimlemenin başladığı indeks (dahil). Varsayılan: 0
stop: Dilimlemenin durduğu indeks (hariç). Varsayılan: Dizinin sonu.
step: Elemanların hangi adımla seçileceği. Varsayılan: 1

[ifade for eleman in koleksiyon if koşul] -> list comprehension

"""
#Listeler ayrıca diğer liste değerlerini de içerebilir.
#Bu listelerin listelerindeki değerlere, aşağıdaki gibi birden fazla dizin kullanılarak erişilebilir:

spam = [['kedi', 'yarasa'], [10, 20, 30, 40, 50]]


print(spam[0]) # ['kedi', 'yarasa']
print(spam[1]) # [10, 20, 30, 40, 50]
print(spam[0][1]) # 'yarasa'
print(spam[1][4]) # "50"
print("\n")
#         0   1   2   3   4   5   6
liste = ["a","b","c","d","e","f","g"]
#        -7  -6  -5  -4  -3  -2  -1

yeniliste = liste[2:5]
yepyeniliste = liste[-5:-1]

# Bu şekilde yeni liste oluştururken [x:y] ifadesinde x dahil, y dahil değildir.

print(yeniliste)
print(yepyeniliste)
print("\n")

bes_sonrasi = liste[5:] # 5. indeksten sonuna kadar al
# [5:]: 5. indeksten başla, sonuna kadar devam et.
ilk_bes = liste[:5] # İlk 5 elemanı al
# [:5]: Başlangıç yok → 0'dan başla, 5'e kadar git (5 dahil değil)

# Ters çevir
ters = liste[::-1] #[::-1]: Baştan başla, ters yönde ilerle.
# Tüm listeyi ikişer ikişer al
ikiser = liste[::2]

print(bes_sonrasi,"\n",ilk_bes,"\n",ters,"\n",ikiser)

print(len(liste))
print(liste[0:]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(liste[0:4]) # ['a', 'b', 'c', 'd']
print(liste[:]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(liste[0:-2]) # ['a', 'b', 'c', 'd', 'e']
print(liste[::]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']


sayac = 0
for i in liste:
    sayac+=1
    print(f"{sayac}. indisdeki eleman {i}", sep="")

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

# append() -> listeye eleman ekler
# insert() -> belirtilen indekse eleman ekler
# remove() -> belirtilen değeri listeden çıkarır
# pop() -> belirtilen indeksteki elemanı listeden çıkarır
# clear() -> listedeki tüm elemanları siler
# index() -> belirtilen değerin indeksini döndürür
# count() -> belirtilen değerin listede kaç defa geçtiğini döndürür
# sort() -> listeyi sıralar
# reverse() -> listeyi ters çevirir
# copy() -> listeyi kopyalar

print(dir(list))

dir([])

method = [i for i in dir(list) if not "_" in i]
print(method)

kardiz = " asdjsakSAJDLASJDA"
kardiz.lower()