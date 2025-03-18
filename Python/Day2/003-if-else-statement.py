'''
yas = int(input("Lutfen yasinizi giriniz: "))

print(f"girilen yas {yas} oldugu icin:")

if yas >= 18 :
    print("Oy Kullanabilirsiniz")
else:
    print("Oy kullanamazsiniz")

    -----------------------------------

puan = int(input("Lutfen puaninizi giriniz: "))

if puan >=85 :
    print("AA ile gectiniz ")
elif (70 <= puan < 85 ):
    print("BB ile gectiniz ")
elif (50 <= puan < 70 ):
    print("CC ile gectiniz ")
else:
    print("Kaldiniz")

    ---------------------------------- 

devamsizlik = int(input("Devamsizlik durumunu giriniz "))

if devamsizlik <= 5:
    disiplin = input("Disiplin cezaniz var mi ? ")
    if disiplin == "Hayır":
        ortalama = int(input("ortalamanizi giriniz: "))
        if 85 <= ortalama:
            print("takdir aldiniz")
        else:
            if 70 <= ortalama < 85:
                print("Tesekkur aldiniz")
            else:
                print("Belge alacak ortalamaya sahip degilsiniz")
    else:
        print("disiplin durumunuz belge almaya engel")
else:
    print("Devamsizlik durumunuz belge almaya engel")

'''
"""

x = 10
y = 20

result = "x büyük" if x > y else "y büyük veya eşit"
print(result)

spam = 0 

if spam < 5 :
    print("Hello World")
    spam = spam + 1

print("spam değeri: ", spam)


while spam < 5:
    print("Hello World")
    spam = spam + 1

print("spam değeri: ", spam)

"""
"""
name = ""
your_name = "SEMİH"

while name != your_name:
    print("Please type your name.")
    name = input()
print("Thank you!")

"""

while True:
    print("Siz kimsiniz")
    name = input()

    if name != "semih":
        continue
    print("Hello, Semih. What is the password? (It is a fish.)")
    password = input()
    if password == "swordfish":
        break
print("Access granted.")

