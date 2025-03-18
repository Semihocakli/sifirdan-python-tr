import keyword

print("Hello World\n")

merhaba = "Merhaba Dünya\n"

print(merhaba)

yasaklı_kelimeler = keyword.kwlist
len(yasaklı_kelimeler)

print(pow(2,3)) # 2 üzeri 3
print(pow(3,2,1)) # 3 üzeri 2 nin 1 e bölümünden kalan

# a = "alice" + 42
# print(a)
a = "alice" + " " + str(42)
print(a)

# a = "alice" * "bob"
# print(a)
# string * string olmaz, string * float olmaz, string * int olur,string * bool olur

# string * boolen
print("alice" * True)
print("alice" * False)



yas = int(input("Lutfen bir yas siniri giriniz:"))
print("\n")
print("------------------")
print("Boolean veri tipi -> 'type(True)':", type(True))
print("Merhaba'nin veri tipi -> 'type(merhaba)':", type(merhaba))
print("Yas'in veri tipi: -> 'type(yas)'", type(yas))
print("------------------\n")
print("------------------")
print("type(123)'un veri tipi -> " , type(123))
print("123*2 ifadesinin degeri:",123*2)
print("type('123')'un veri tipi ->", type("123"))
print("'123'*2 degerinin degeri:","123"*2)
print("------------------\n")

print(f"girilen yas {yas} oldugu icin:")

if yas >= 18 :
    print("Oy Kullanabilirsiniz")
else:
    print("Oy kullanamazsiniz")

'''

 BURASI YORUM SATIRLARIDIR 

 Bir sayının dize değeri, tam sayı veya kayan noktalı versiyonundan tamamen farklı bir değer olarak kabul edilmesine rağmen, bir tam sayı bir kayan noktaya eşit olabilir.

>>> 42 == '42'
Yanlış
>>> 42 == 42.0
Doğru
>>> 42.0 == 0042.000
Doğru

Python bu ayrımı yapar çünkü dizeler metindir, tam sayılar ve kayan noktalı sayılar ise sayıdır.

'''

print("Semih" + " " + "Ocaklı")

isim = "Semih"
print("Atama Öncesi İsim:",isim)
isim += " " + "Ocaklı"
print("Atama Sonrası İsim:",isim)

print("------------------")

a = 2
print("ATAMA YAPTIGIMIZ A' NIN DEGERİ",a)
a += 2
print("ATAMA SONRASI A' NIN DEGERİ:",a)

print("isim:",isim , 
      "yas:", yas ,
      )

#    print('Bir yıl sonra ' + (int(yas) + 1) + ' yaşında olacaksın.') -> bu kullanım yanlıştır çünkü 
"""
Burada int(yas) + 1 işleminin sonucu integer (tam sayı) bir değerdir. 
Ancak + operatörü ile bir string (metin) ile birleştirilmeye çalışılıyor. 
Python'da bir string ile bir int doğrudan birleştirilemez
"""
print('Bir yıl sonra ' + str(int(yas) + 1) + ' yaşında olacaksın.')

print(f'Bir yıl sonra {int(yas) + 1} yaşında olacaksın.')

print("\n")
print("http://", "www.", "istihza.", "com", sep="")
# "sep" -> parametresi, ekrana basılacak öğeler arasına hangi karakterin yerleştirileceğini gösterir. 
# Bu parametrenin öntanımlı değeri bir adet boşluk karakteridir (” “).
print("http://", "www", "istihza", "com", sep=".")
print("\n")

print("bir", "iki", "üç", "dört", "on dört", sep="mumdur,")

print("bir", "iki", "üç", "dört", "on dört", sep=" " + "mumdur" + " ")

print("birinci satır", "ikinci satır", "üçüncü satır", sep="\n")

"""
İfade (Expression): Bir değer döndüren kod parçalarıdır. Örneğin: 5 + 3, 10 * 2.
İfade Cümlesi (Statement): Python'da bir işlemi gerçekleştiren, ancak değer döndürmeyen komutlardır. 
Örneğin: spam = 10 bir atama cümlesidir.
"""

dosya = open("deneme.txt", "w")
print("Ben Python, Monty Python!", file=dosya)
dosya.close()
# print bir dosyaya da yazılabilir. Bunun için print fonksiyonunun file parametresi kullanılır.
# flush = true kullanırsak dosyaya her yeni bir şey eklediğimizde dosyayı kapatıp tekrar açmamıza gerek kalmaz.

print(*"Galatasaray") # G a l a t a s a r a y 

print("{} ve {} iyi bir ikilidir".format("Python", "Django"))