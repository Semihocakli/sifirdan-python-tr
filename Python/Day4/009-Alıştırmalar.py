'''
1.) Bir menü programı oluşturunuz. (kategori ve yemek alt kategorileri tanımlayarak)
menu = {
    "Kategoriler": {
        "Kahvaltı": {
            "Menemen": 15,
            "Simit": 2,
            "Çay": 1.5
        },
        "Öğle Yemeği": {
            "Izgara Tavuk": 20,
            "Köfte": 18,
            "Pilav": 5
        },
        "Akşam Yemeği": {
            "Döner": 12,
            "Lahmacun": 7,
            "Pide": 10
        }
    }
}

print("Menü:")
for kategori, yemekler in menu["Kategoriler"].items():
    print(kategori + ":")
    for yemek, fiyat in yemekler.items():
        print(f"- {yemek}: {fiyat} TL")
'''
'''
2.) Yukarıdaki örneği fiyatlı yemeklerin fiyatları olacak şekilde güncelleyiniz. (Menü oluşturmak için siz manuel giriş yapınız)
'''
'''

3.) Yukarıdaki örneği bir sipariş haline getirip, kullanıcının seçtiği yemekler için ödeyecek olduğu hesabı belirten hale getiriniz. (Hazır bir menü sistemi oluşturup hesaplamaları yapınız. Önceki çıktıları kullanabilirsiniz)
'''
'''
secim = input("Lütfen istediğiniz kategoriyi seçin (Kahvaltı, Öğle Yemeği, Akşam Yemeği): ").strip()

if secim in menu["Kategoriler"]:
    siparisler = {}
    while True:
        yemek_secim = input(f"Sipariş vermek istediğiniz yemeği seçin ({secim} kategorisinden çıkmak için 'q' tuşuna basın): ").strip()
        
        if yemek_secim.lower() == 'q':
            break
        
        if yemek_secim in menu["Kategoriler"][secim]:
            if yemek_secim in siparisler:
                siparisler[yemek_secim] += 1
            else:
                siparisler[yemek_secim] = 1
        else:
            print("Geçerli bir yemek seçimi yapmadınız.")

    toplam_tutar = 0
    for yemek, adet in siparisler.items():
        fiyat = menu["Kategoriler"][secim][yemek]
        toplam_tutar += fiyat * adet

    print("Siparişleriniz:")
    for yemek, adet in siparisler.items():
        print(f"{yemek}: {adet} adet")
    print(f"Toplam Tutar: {toplam_tutar} TL")
else:
    print("Geçerli bir kategori seçimi yapmadınız.")

4.) Bir öğrenci tanıma kartı oluşturunuz. öğrenciye adi, soyadı gibi bilgileri sorduktan sonra, derslerini ve derslerine ait notları sorup toplu çıktı veren bir sistem yazınız. (bir nevi cv gibi)

ogrenci = {
    "Kimlik": {
        "Adi": "",
        "Soyadi": "",
        "Yasi": ""
    },
    "Egitim": {
        "ilkokul": "",
        "ortaokul": "",
        "lise": "",
        "universite": "",
    },
    "Bolum_Notlari": {
        "Algoritma_ve_Programlama": "",
        "Temel_Elektronik": "",
        "Bilgisayara_Giris": "",
    }
}

# Öğrenci bilgilerini döngü kullanarak almak
for kategori, alt_bilgiler in ogrenci.items():
    print(f"{kategori} Bilgileri:")
    for alt_kategori, deger in alt_bilgiler.items():
        ogrenci[kategori][alt_kategori] = input(f"{alt_kategori}: ")


print("\n-------------------------------------------------------")   
print("\nÖğrenci Bilgileri:")
print(f"Adı: {ogrenci['Kimlik']['Adi']}")
print(f"Soyadı: {ogrenci['Kimlik']['Soyadi']}" )
print(f"Yaşı: {ogrenci['Kimlik']['Yasi']}")

print("\nEğitim Bilgileri:")
print(f"İlkokul: {ogrenci['Egitim']['ilkokul']}")
print(f"Ortaokul: {ogrenci['Egitim']['ortaokul']}")
print(f"Lise: {ogrenci['Egitim']['lise']}")
print(f"Üniversite: {ogrenci['Egitim']['universite']}")

print("\nBölüm Notları:")
print(f"Algoritma ve Programlama: {ogrenci['Bolum_Notlari']['Algoritma_ve_Programlama']}")
print(f"Temel Elektronik: {ogrenci['Bolum_Notlari']['Temel_Elektronik']}")
print(f"Bilgisayara Giriş: {ogrenci['Bolum_Notlari']['Bilgisayara_Giris']}")

'''
'''
5.) Bir todo list oluşturunuz. oluşturacak olduğunuz yapılacaklar listesinde kullanıcıya görevleri sorunuz, görev listesini yapınız, görevlerin durumunu kontrol ediniz ve tüm görevler tamamlanınca teşekkür ederek programı tamamlayınız.
'''


'''
6.) Yukarıdaki örnek için görev kategorileri tanımlayarak örneği tekrar yapınız.
'''
'''
7.) Yukarıda ki örneği görev kategori ve alt görevler şeklinde güncelleyerek tekrar yapınız.
'''
'''
8.) Kullanıcıdan n tane sayı girmesini isteyerek, hangi sayıyı kaçar tane girdiğini kullanıcıya söyleyen programı yazınız.

n = int(input("Kaç tane sayı gireceksiniz: "))

sayilar = []
for i in range(n):
    sayi = int(input(f"{i+1}. sayıyı giriniz: "))
    sayilar.append(sayi)

girilen_sayilar = {}
for sayi in sayilar:
    if sayi in girilen_sayilar:
        girilen_sayilar[sayi] += 1
    else:
        girilen_sayilar[sayi] = 1

print("Sayıların frekansları:")
for sayi, frekans in girilen_sayilar.items():
    print(f"n:{sayi} - {frekans} kez")

'''
'''
9.) Kullanıcıya en sevdiği yazarları ve bu yazarlara ait en sevdiği eserleri sorarak, aldığı verileri gruplar halinde listeyen uygulamayı yazınız.

# Boş bir sözlük oluşturarak verileri gruplamak için kullanacağız.
yazarlar_ve_eserleri = {}

while True:
    yazar = input("En sevdiğiniz yazarın adını girin (Çıkmak için 'q' tuşuna basın): ")
    
    if yazar.lower() == 'q':
        break  # Kullanıcı 'q' tuşuna bastığında döngüyü sonlandırır.
    
    eser = input(f"{yazar} adlı yazarın en sevdiğiniz eserini girin: ")
    
    # Yazarı ve eseri sözlüğe ekler
    if yazar in yazarlar_ve_eserleri:
        yazarlar_ve_eserleri[yazar].append(eser)
    else:
        yazarlar_ve_eserleri[yazar] = [eser]

# Kullanıcının girdiği verileri gruplar halinde listeleyelim.
print("\nKullanıcının En Sevdiği Yazarlar ve Eserleri:")
for yazar, eserler in yazarlar_ve_eserleri.items():
    print(f"{yazar}:")
    for eser in eserler:
        print(f"- {eser}")

'''
'''
10.) 2 den 1000'e kadar olan asal sayıları bulan ve listeleyen programı yazınız.
'''
asal_sayilar = []

for sayi in range(2, 1001):
    # Sayının asal olup olmadığını kontrol etmek için bir bayrak (flag) kullanalım
    asal_mi = True
    
    # Sayının 2'den kendisine kadar olan bölenlerini kontrol edelim
    for bolen in range(2, int(sayi ** 0.5) + 1):
        if sayi % bolen == 0:
            asal_mi = False
            break
    
    # Sayı asalsa, listeye ekleyelim
    if asal_mi:
        asal_sayilar.append(sayi)

# Asal sayıları listeleyelim
print("2'den 1000'e kadar olan asal sayılar:")
print(asal_sayilar)
