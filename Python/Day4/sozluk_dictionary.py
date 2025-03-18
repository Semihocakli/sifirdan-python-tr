# dictionary, key-value ile {key: value} şeklinde tanımlanır.


myCat = {'size': 'fat', 
         'color': 'gray', 
         'disposition': 'loud'}

# print(myCat['size']) # fat

for i in myCat:
    print(myCat[i]) # fat gray loud
    # print(i) # size color disposition
    # print([i]) # ['size'] ['color'] ['disposition']

telefon_defteri = {"ahmet öz" : "0532 532 32 32",
                   "mehmet su": "0543 543 42 42",
                   "seda naz" : "0533 533 33 33",
                   "eda ala"  : "0212 212 12 12"}

kişi = input("Telefon numarasını öğrenmek için bir kişi adı girin: ")

cevap = "{} adlı kişinin telefon numarası: {}"

print(cevap.format(kişi, telefon_defteri[kişi]))

# keys() -> dictionary içindeki key'leri döndürür
# values() -> dictionary içindeki value'ları döndürür
# items() -> dictionary içindeki key-value çiftlerini döndürür
# get() -> belirtilen key'in value'sunu döndürür
# setdefault() -> belirtilen key'in value'sunu döndürür, eğer key yoksa belirtilen değeri ekler
# update() -> dictionary içindeki key-value çiftlerini günceller
# clear() -> dictionary içindeki tüm elemanları siler
# copy() -> dictionary'yi kopyalar
# pop() -> belirtilen key'i siler ve value'sunu döndürür
# popitem() -> dictionary içindeki son key-value çiftini siler ve döndürür
# fromkeys() -> belirtilen key'lerin value'larını belirtilen değer yapar


print(telefon_defteri.keys()) # dict_keys(['ahmet öz', 'mehmet su', 'seda naz', 'eda ala'])
print(telefon_defteri.values()) # dict_values(['0532 532 32 32', '0543 543 42 42', '0533 533 33 33', '0212 212 12 12'])
print(telefon_defteri.items()) # dict_items([('ahmet öz', '0532 532 32 32'), ('mehmet su', '0543 543 42 42'), ('seda naz', '0533 533 33 33'), ('eda ala', '0212 212 12 12')])
print(telefon_defteri.get("ahmet öz")) # 0532 532 32 32
print(telefon_defteri.setdefault("ahmet öz", "Bulunamadı")) # 0532 532 32 32
print(telefon_defteri.pop("ahmet öz")) # 0532 532 32 32

# iç içe geçmiş dictionary 

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


import pprint

spam = {'name': 'Alice', 'age': 30, 'hobbies': ['reading', 'coding']}
pprint.pprint(spam)

import pprint

harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
sozluk = {}

for i in harfler:
    sozluk[i] = harfler.index(i)

pprint.pprint(sozluk)


# dictionary comprehension
import pprint

harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
sozluk = {i: harfler.index(i) for i in harfler}

pprint.pprint(sozluk)
