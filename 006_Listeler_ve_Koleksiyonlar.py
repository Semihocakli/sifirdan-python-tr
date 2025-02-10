# Python'da Listeler ve Koleksiyonlar
# ================================

"""
KOLEKSIYON YAPILARI
------------------
Python'da temel koleksiyon yapıları:
1. Listeler (Lists)
2. Demetler (Tuples)
3. Kümeler (Sets)
4. Sözlükler (Dictionaries)
"""

# 1. LİSTELER (LISTS)
# ------------------
print("1. LİSTELER\n")

# 1.1 Liste Oluşturma
bos_liste = []
sayilar = [1, 2, 3, 4, 5]
karisik_liste = [1, "Python", 3.14, True]
ic_ice_liste = [1, [2, 3], [4, 5, 6]]


print("Liste örnekleri:")
print(f"Boş liste: {bos_liste}")
print(f"Sayı listesi: {sayilar}")
print(f"Karışık liste: {karisik_liste}")
print(f"İç içe liste: {ic_ice_liste}")

# 1.2 Liste Metodları
print("\n1.2 Liste Metodları:")
meyveler = ["elma", "armut", "muz"]
print(f"Orijinal liste: {meyveler}")

# Eleman ekleme
meyveler.append("kiraz")
print(f"append() sonrası: {meyveler}")

meyveler.insert(1, "portakal")
print(f"insert() sonrası: {meyveler}")

# Eleman silme
silinen = meyveler.pop()
print(f"pop() sonrası: {meyveler}, silinen: {silinen}")

meyveler.remove("armut")
print(f"remove() sonrası: {meyveler}")

# Liste birleştirme
diger_meyveler = ["karpuz", "kavun"]
meyveler.extend(diger_meyveler)
print(f"extend() sonrası: {meyveler}")

# 1.3 Liste Dilimleme (Slicing)
print("\n1.3 Liste Dilimleme:")
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Orijinal liste: {sayilar}")
print(f"İlk 3 eleman: {sayilar[:3]}")
print(f"Son 3 eleman: {sayilar[-3:]}")
print(f"Ortadaki elemanlar: {sayilar[3:7]}")
print(f"İkişer atlayarak: {sayilar[::2]}")
print(f"Tersten: {sayilar[::-1]}")
print(f"İlk 3 elemanı atla: {sayilar[3:]}")
print(f"İlk 3 elemanı atla ve tersten: {sayilar[3::-1]}")
""" 
    0  1  2  3  4  5  6 
    s  a  y  i  l  a  r 
   -1 -2 -3 -4 -5 -6 -7
""" 
# 2. DEMETLER (TUPLES)
# -------------------
print("\n2. DEMETLER\n")


# 2.1 Demet Oluşturma
tekli_demet = (1,)  # Tek elemanlı demet için virgül önemli!
sayilar_demet = (1, 2, 3, 4, 5)
karisik_demet = (1, "Python", 3.14, True)

print("Demet örnekleri:")
print(f"Tekli demet: {tekli_demet}")
print(f"Sayı demeti: {sayilar_demet}")
print(f"Karışık demet: {karisik_demet}")

# 2.2 Demet vs Liste
print("\n2.2 Demet vs Liste:")
from sys import getsizeof

liste = [1, 2, 3, 4, 5]
demet = (1, 2, 3, 4, 5)

print(f"Liste bellek kullanımı: {getsizeof(liste)} bytes")
print(f"Demet bellek kullanımı: {getsizeof(demet)} bytes")

# 3. KÜMELER (SETS)
# ---------------
print("\n3. KÜMELER\n")

# 3.1 Küme Oluşturma
kume1 = {1, 2, 3, 4, 5}
kume2 = {4, 5, 6, 7, 8}
tekrarli = {1, 2, 2, 3, 3, 4}  # Tekrar eden elemanlar otomatik silinir

print("Küme örnekleri:")
print(f"Küme 1: {kume1}")
print(f"Küme 2: {kume2}")
print(f"Tekrarlı küme: {tekrarli}")

# 3.2 Küme İşlemleri
print("\n3.2 Küme İşlemleri:")
print(f"Birleşim: {kume1 | kume2}")
print(f"Kesişim: {kume1 & kume2}")
print(f"Fark (kume1 - kume2): {kume1 - kume2}")
print(f"Simetrik fark: {kume1 ^ kume2}")

# 4. SÖZLÜKLER (DICTIONARIES)
# -------------------------
print("\n4. SÖZLÜKLER\n")

# 4.1 Sözlük Oluşturma
bos_sozluk = {}
ogrenci = {
    "ad": "Ahmet",
    "yas": 20,
    "dersler": ["Matematik", "Fizik", "Python"],
    "mezun": False
}

print("Sözlük örnekleri:")
print(f"Boş sözlük: {bos_sozluk}")
print(f"Öğrenci sözlüğü: {ogrenci}")

# 4.2 Sözlük İşlemleri
print("\n4.2 Sözlük İşlemleri:")

# Değer ekleme/güncelleme
ogrenci["bolum"] = "Bilgisayar Mühendisliği"
ogrenci["yas"] = 21

# Değer silme
del ogrenci["mezun"]

print("Güncellenmiş sözlük:")
for anahtar, deger in ogrenci.items():
    print(f"{anahtar}: {deger}")

# 4.3 İç İçe Sözlükler
print("\n4.3 İç İçe Sözlükler:")
okul = {
    "9A": {
        "sinif_ogretmeni": "Ayşe Hoca",
        "ogrenci_sayisi": 30,
        "dersler": ["Matematik", "Fizik", "Kimya"]
    },
    "9B": {
        "sinif_ogretmeni": "Mehmet Hoca",
        "ogrenci_sayisi": 28,
        "dersler": ["Biyoloji", "Fizik", "Kimya"]
    }
}

print("Okul bilgileri:")
for sinif, bilgiler in okul.items():
    print(f"\n{sinif} Sınıfı:")
    for anahtar, deger in bilgiler.items():
        print(f"  {anahtar}: {deger}")

"""
ÖZET VE KULLANIM İPUÇLARI
------------------------
1. Liste: Sıralı, değiştirilebilir koleksiyon
   - En çok kullanılan veri yapısı
   - Dinamik boyut
   - Herhangi bir veri tipi tutabilir

2. Demet: Sıralı, değiştirilemez koleksiyon
   - Performans avantajı
   - Veri bütünlüğü garantisi
   - Anahtar olarak kullanılabilir

3. Küme: Sırasız, benzersiz elemanlar
   - Hızlı üyelik testi
   - Matematiksel küme işlemleri
   - Tekrar eden elemanları temizleme

4. Sözlük: Anahtar-değer çiftleri
   - Hızlı erişim
   - Esnek veri yapısı
   - JSON benzeri yapı

İYİ UYGULAMALAR
--------------
1. Doğru veri yapısını seçin
2. Büyük veriler için liste yerine küme kullanın
3. Değişmez veriler için demet tercih edin
4. Sözlüklerde anlamlı anahtar isimleri kullanın
5. İç içe yapılarda okunabilirliğe dikkat edin
""" 