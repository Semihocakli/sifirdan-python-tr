''' 
with open("deneme.txt", "a") as f:
    f.write("slkdflsadklş")

# Dosyayı "r" (read) modunda açıp veriyi okuyoruz
with open("deneme.txt", "r") as f:
    print(f.read())

'''# Dosyayı "a" (append) modunda açıp veri yazıyoruz
# oyun tasarla oyun için 1 istatistiler için 2 
import random

numara = random.randint(1, 50)
tahmin_hakki = 5

tahminler = []

print("Sayı Tahmin Oyununa Hoş Geldiniz!")
print(f"1 ile 50 arasında bir sayı tuttum. {tahmin_hakki} hakkınız var.")

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
        tahminler.append(cevap)
        break
    
    tahminler.append(cevap)

if cevap != numara:
    print(f"Üzgünüm, doğru sayıyı tahmin edemediniz. Doğru sayı: {numara}")

# Tahminleri dosyada tutma
with open("tahminler.txt", "w") as dosya:
    for i, tahmin in enumerate(tahminler):
        dosya.write(f"{i+1}. tahmin: {tahmin}\n")
