# global degisken ve local degisken

x = 5 # global degisken

def fonksiyon():
    y = 10 # local degisken
    x = 10
    print(x) # 10
    print(y) # 10

print(x) # 5
fonksiyon()
print(x) # 5

print("")

x = 5 # global degisken

def fonksiyon():
    y = 10 # local degisken
    global x
    x = 10

    print(y) # 10

print(x) # 5
fonksiyon()
print(x) # 10

print("")

# Python’da bir fonksiyonun yaşam döngüsü iki aşamadan oluşur: Tanımlanma ve çağrılma.

def sistem_bilgisi_göster():
    import sys
    print("\nSistemde kurulu Python'ın;")
    print("\tana sürüm numarası:", sys.version_info.major)
    print("\talt sürüm numarası:", sys.version_info.minor)
    print("\tminik sürüm numarası:", sys.version_info.micro)

    print("\nKullanılan işletim sisteminin;")
    print("\tadı:", sys.platform)

sistem_bilgisi_göster()

def ogrenci_bilgileri(adi, soyadi, numara):
    print("\nÖğrenci Bilgileri")
    print("\tAdı:", adi)
    print("\tSoyadı:", soyadi)
    print("\tNumarası:", numara)

ogrenci_bilgileri("Ahmet", "Yılmaz", 12345)

def toplam(a, b):
    toplam = a + b
    return toplam

print(toplam(5, 10))

print( "-"*50)

def toplam(a, b):
    toplam = a + b
    print(toplam)

toplam(5, 10)

def cube(num):
    return num*num*num 

sayi = 5
kup = cube(sayi)
print(kup)

# gömülü fonksiyonlar

# abs() fonksiyonu, mutlak değer almak için kullanılır.
# raund() fonksiyonu, bir sayıyı yuvarlamak için kullanılır.
# max() fonksiyonu, en büyük sayıyı bulmak için kullanılır.
# min() fonksiyonu, en küçük sayıyı bulmak için kullanılır.
# sum() fonksiyonu, sayıların toplamını bulmak için kullanılır.
# pow() fonksiyonu, üs alma işlemi için kullanılır.
# len() fonksiyonu, bir listenin uzunluğunu bulmak için kullanılır.
# zip() fonksiyonu, iki listeyi birleştirmek için kullanılır.
# type() fonksiyonu, bir nesnenin türünü bulmak için kullanılır.
# id() fonksiyonu, bir nesnenin kimliğini bulmak için kullanılır.
# eval() fonksiyonu, bir metni Python koduna dönüştürmek için kullanılır.
# exec() fonksiyonu, bir metni Python kodu olarak çalıştırmak için kullanılır.
# globals() fonksiyonu, global değişkenleri bulmak için kullanılır.
# locals() fonksiyonu, yerel değişkenleri bulmak için kullanılır.

# enumerate() fonksiyonu, bir diziye numaralandırma eklemek için kullanılır.

liste = ['elma', 'armut', 'kiraz']

for index, value in enumerate(liste):
    print(index, value)


# map() fonksiyonu, bir fonksiyonu bir diziye uygulamak için kullanılır.
def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

print(squared_numbers)


# filter() fonksiyonu, bir diziye bir filtre uygulamak için kullanılır.
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))

print(even_numbers)

# lambda fonksiyonları
# lambda fonksiyonları, adı olmayan ve tek satırda tanımlanan fonksiyonlardır.

# lambda parametreler: ifade

# iki sayının toplamını hesaplayan lambda fonksiyonu
toplam = lambda a, b: a + b
print(toplam(5, 10)) # 15

# bir sayının karesini hesaplayan lambda fonksiyonu
karesi = lambda x: x * x
print(karesi(5)) # 25

# bir listenin her elemanının karesini hesaplayan lambda fonksiyonu
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]

# bir listenin çift elemanlarını filtreleyen lambda fonksiyonu
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # [2, 4]

# sorted() fonksiyonu, bir listeyi sıralamak için kullanılır.
unsorted_list = [5, 2, 9, 1, 5, 6]
sorted_list = sorted(unsorted_list)
print(sorted_list) # [1, 2, 5, 5, 6, 9]

# sorted() fonksiyonu, bir listeyi tersine sıralamak için kullanılır.
sorted_list_desc = sorted(unsorted_list, reverse=True)
print(sorted_list_desc) # [9, 6, 5, 5, 2, 1]
# reversed() fonksiyonu, bir listeyi tersine çevirmek için kullanılır.

# recursive fonksiyonlar
# Recursive fonksiyonlar, kendini çağıran fonksiyonlardır.
# Recursive fonksiyonlar, bir problemi daha küçük parçalara bölerek çözmek için kullanılır.

def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)
    
sayi = int(input("Lutfen bir sayi giriniz: "))
sonuc = faktoriyel(sayi)
print(f"{sayi} faktoriyel = {sonuc}")

# iç içe fonksiyonlar

def dış_fonksiyon():

    def iç_fonksiyon():
        print("İç fonksiyon çalıştı.")

    print("Dış fonksiyon çalıştı.")
    iç_fonksiyon()

dış_fonksiyon()

# fonksiyonlar, Python'da birinci sınıf nesnelerdir.
# Birinci sınıf nesneler, diğer nesnelerle aynı şekilde kullanılabilen nesnelerdir.
# Birinci sınıf nesneler, değişkenlere atanabilir, fonksiyonlardan döndürülebilir ve fonksiyonlara parametre olarak geçirilebilir.

def topla(a, b):

    return a + b

def çıkar(a, b):

    return a - b

def işlem(fonksiyon, a, b):

    return fonksiyon(a, b)

print(işlem(topla, 5, 10)) # 15
print(işlem(çıkar, 5, 10)) # -5

# üreteçler (generators)
# Üreteçler, bellekte yer kaplamadan veri üreten fonksiyonlardır.
# Üreteçler, yield anahtar kelimesi ile tanımlanır.

def sayı_üret():
    for i in range(5):
        yield i

sayılar = sayı_üret()

for sayı in sayılar:
    print(sayı)

# yield from ifadesi, bir üreteçten değerleri başka bir üretece aktarmak için kullanılır.


# bezeyici (decorator) fonksiyonlar
# Bezeyici fonksiyonlar, diğer fonksiyonları değiştirmek veya genişletmek için kullanılır.
# Bezeyici fonksiyonlar, diğer fonksiyonları parametre olarak alır ve yeni bir fonksiyon döndürür.

def bezeyici(fonksiyon):
    
    def wrapper():
        print("Fonksiyon çalıştı.")
        fonksiyon()
        print("Fonksiyon bitti.")

    return wrapper

def fonksiyon():
    print("Merhaba, dünya!")

bezeyici_fonksiyon = bezeyici(fonksiyon)
bezeyici_fonksiyon()

# next fonksiyonu

def sayı_üret():
    for i in range(5):
        yield i

sayılar = sayı_üret()

print(next(sayılar)) # 0
print(next(sayılar)) # 1
print(next(sayılar)) # 2