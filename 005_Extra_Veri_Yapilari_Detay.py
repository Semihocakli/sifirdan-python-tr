# Python Veri Yapıları - İleri Seviye Detaylar
# =========================================

"""
Bu dosyada, Python'daki veri yapılarının ileri seviye özelliklerini,
performans karakteristiklerini ve en iyi kullanım senaryolarını inceleyeceğiz.
"""

# 1. ZAMAN KARMAŞİKLİĞİ VE VERİ YAPILARI
# -------------------------------------
from timeit import timeit
import sys
from collections import deque, defaultdict, Counter, OrderedDict
import array

print("1. Veri Yapılarının Zaman Karmaşıklığı\n")

# Liste vs Deque Performans Karşılaştırması
def liste_basina_ekleme():
    liste = []
    for i in range(1000):
        liste.insert(0, i)

def deque_basina_ekleme():
    d = deque()
    for i in range(1000):
        d.appendleft(i)

liste_suresi = timeit(liste_basina_ekleme, number=100)
deque_suresi = timeit(deque_basina_ekleme, number=100)

print(f"Liste başına ekleme süresi: {liste_suresi:.4f} saniye")
print(f"Deque başına ekleme süresi: {deque_suresi:.4f} saniye")

# 2. BELLEK VERİMLİLİĞİ
# --------------------
print("\n2. Bellek Verimliliği\n")

# Normal liste vs Array karşılaştırması
normal_liste = list(range(1000))
array_liste = array.array('i', range(1000))

print(f"Normal liste bellek kullanımı: {sys.getsizeof(normal_liste)} bytes")
print(f"Array bellek kullanımı: {sys.getsizeof(array_liste)} bytes")

# 3. ÖZEL KOLEKSİYON TİPLERİ
# -------------------------
print("\n3. Özel Koleksiyon Tipleri\n")

# 3.1 defaultdict kullanımı
print("3.1 defaultdict Örneği:")
normal_dict = {}
kelimeler = ["elma", "armut", "elma", "kiraz", "armut", "elma"]

# Normal dictionary ile kelime sayısı bulma
for kelime in kelimeler:
    if kelime in normal_dict:
        normal_dict[kelime] += 1
    else:
        normal_dict[kelime] = 1

# defaultdict ile kelime sayısı bulma
otomatik_dict = defaultdict(int)
for kelime in kelimeler:
    otomatik_dict[kelime] += 1

print(f"Normal dict sonucu: {dict(normal_dict)}")
print(f"defaultdict sonucu: {dict(otomatik_dict)}")

# 3.2 Counter kullanımı
print("\n3.2 Counter Örneği:")
sayac = Counter(kelimeler)
print(f"Counter sonucu: {dict(sayac)}")
print(f"En çok tekrar eden 2 eleman: {sayac.most_common(2)}")

# 3.3 OrderedDict vs Normal Dict
print("\n3.3 OrderedDict vs Normal Dict:")
normal = {}
sirali = OrderedDict()

normal['a'] = 1
normal['b'] = 2
normal['c'] = 3

sirali['a'] = 1
sirali['b'] = 2
sirali['c'] = 3

print(f"Normal dict: {normal}")
print(f"OrderedDict: {sirali}")

# 4. SET OPERASYONLARI VE PERFORMANS
# -------------------------------
print("\n4. Set Operasyonları ve Performans\n")

set1 = set(range(1000))
set2 = set(range(500, 1500))

# Set operasyonlarının performansı
def olcum_yap(islem, set1, set2):
    return timeit(lambda: islem(set1, set2), number=1000)

birlesim_suresi = olcum_yap(lambda x, y: x | y, set1, set2)
kesisim_suresi = olcum_yap(lambda x, y: x & y, set1, set2)
fark_suresi = olcum_yap(lambda x, y: x - y, set1, set2)

print(f"Birleşim işlemi süresi: {birlesim_suresi:.6f} saniye")
print(f"Kesişim işlemi süresi: {kesisim_suresi:.6f} saniye")
print(f"Fark işlemi süresi: {fark_suresi:.6f} saniye")

# 5. LİSTE PERFORMANS İYİLEŞTİRMELERİ
# --------------------------------
print("\n5. Liste Performans İyileştirmeleri\n")

# 5.1 Liste Ön Tahsisi
print("5.1 Liste Ön Tahsisi:")
def kotu_yontem():
    liste = []
    for i in range(10000):
        liste.append(i)

def iyi_yontem():
    liste = [None] * 10000
    for i in range(10000):
        liste[i] = i

kotu_sure = timeit(kotu_yontem, number=100)
iyi_sure = timeit(iyi_yontem, number=100)

print(f"Ön tahsis yapılmadan: {kotu_sure:.4f} saniye")
print(f"Ön tahsis yapılarak: {iyi_sure:.4f} saniye")

# 6. DİCT PERFORMANS İPUÇLARI
# -------------------------
print("\n6. Dict Performans İpuçları\n")

# 6.1 Dict Anahtarlarının Performansı
class KotuAnahtar:
    def __init__(self, deger):
        self.deger = deger
    
    def __hash__(self):
        # Kötü hash fonksiyonu - çakışmalara yol açar
        return 1

class IyiAnahtar:
    def __init__(self, deger):
        self.deger = deger
    
    def __hash__(self):
        # İyi hash fonksiyonu
        return hash(self.deger)

# 7. ÖZET VE PERFORMANS KARŞILAŞTIRMALARI
# ------------------------------------
print("\n7. Özet ve Performans Karşılaştırmaları\n")

"""
VERİ YAPISI SEÇİM REHBERİ
-------------------------
1. Liste (list) kullanın, eğer:
   - Sıralı veriye ihtiyacınız varsa
   - Elemanları değiştirmeniz gerekiyorsa
   - Tekrar eden elemanlara izin veriliyorsa

2. Tuple kullanın, eğer:
   - Değişmez (immutable) veriye ihtiyacınız varsa
   - Performans kritikse (listeden daha hızlıdır)
   - Veri bütünlüğü önemliyse

3. Set kullanın, eğer:
   - Benzersiz elemanlara ihtiyacınız varsa
   - Küme işlemleri yapacaksanız (birleşim, kesişim, fark)
   - Eleman varlığı kontrolü sık yapılacaksa (O(1) performans)

4. Dictionary kullanın, eğer:
   - Anahtar-değer ilişkisi gerekiyorsa
   - Hızlı erişim önemliyse (O(1) performans)
   - Veri eşleştirmesi yapılacaksa

5. Deque kullanın, eğer:
   - Baştan ve sondan ekleme/çıkarma işlemleri sık yapılacaksa
   - FIFO veya LIFO yapısı gerekiyorsa

6. Array kullanın, eğer:
   - Bellek kullanımı kritikse
   - Sayısal verilerle çalışıyorsanız
   - Numpy gibi bilimsel hesaplama kütüphaneleriyle entegrasyon gerekiyorsa

PERFORMANS İPUÇLARI
------------------
1. Doğru veri yapısını seçmek, performansı dramatik şekilde etkiler
2. Bellek kullanımı ve işlem hızı arasındaki dengeyi gözetin
3. Büyük veri setlerinde generator kullanmayı düşünün
4. Hash tabanlı yapılar (dict, set) arama işlemleri için idealdir
5. Liste birleştirme işlemlerinde extend() metodunu tercih edin
6. Dictionary ve set için iyi hash fonksiyonları kullanın
7. Sık erişilen verileri önbelleğe almayı düşünün
""" 