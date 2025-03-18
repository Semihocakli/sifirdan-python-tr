import math
import random
import datetime

# a = 90

# print(math.sin(a))

# print(random.random())
# print(random.randrange(start=1,stop=5))
'''
numara = random.randint(1, 50)  
tahmin_hakki = 5  

print("Sayı Tahmin Oyununa Hoş Geldiniz!")
print(f"0 ile 50 arasında bir sayı tuttum. {tahmin_hakki} hakkınız var.")

for a in range(1, tahmin_hakki + 1):
    cevap = int(input(f"{a}. tahmininizi yapın: "))
    
    if cevap < 1 or cevap > 50:
        print("Lütfen 1 ile 50 arasında bir sayı giriniz.")
    elif cevap < numara:
        print("Daha yüksek bir sayı tahmin edin.")
    elif cevap > numara:
        print("Daha düşük bir sayı tahmin edin.")
    else:
        print(f"Tebrikler! Doğru tahmin ettiniz. Sayı: {numara}")
        break

if cevap != numara:
    print(f"Üzgünüm, doğru sayıyı tahmin edemediniz. Doğru sayı: {numara}")

tahmin_Sayisi = 0
tutulan_sayi = 85 
alt_sinir = 1
ust_sinir = 100
tahmin = random.randint(alt_sinir, ust_sinir)  

while tahmin != tutulan_sayi:
    tahmin_Sayisi += 1
    print(f"{tahmin_Sayisi}.Tahmin sayısı {tahmin}")
    if tahmin < tutulan_sayi:
        print(f"{tahmin} sayısı çok düşük.")
        alt_sinir = tahmin +1
    else:
        print(f"{tahmin} sayısı çok yüksek.")
        ust_sinir = tahmin -1
    
    tahmin = random.randint(alt_sinir, ust_sinir)

print(f"Tebrikler! Bilgisayar {tutulan_sayi} sayısını tahmin etti.")

'''
'''

import time

geri_sayim = 60

while geri_sayim > 0:
    print(geri_sayim)
    geri_sayim -= 1
    time.sleep(1)  
else:
    print("Geri sayım tamamlandı!")

import time

geri_sayim = 5
while geri_sayim > 0:
    geri_sayim -= 1
    time.sleep(5)
    print("Adini yaz")
else:
    print("Geri sayım tamamlandi")

'''
import time

start_time = time.time()

print("Asal Sayılar:")
for num in range(2, 1001):
    bölünme = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            bölünme = False
            break
    if bölünme:
        print(num)
        time.sleep(0.01)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Program çalışma süresi: {elapsed_time:.6f} saniye")

