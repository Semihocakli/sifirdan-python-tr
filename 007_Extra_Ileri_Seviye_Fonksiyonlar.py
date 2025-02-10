# Python'da İleri Seviye Fonksiyon Kullanımı
# =====================================

"""
Bu dosyada, fonksiyonların daha ileri seviye kullanımlarını ve 
nesne yönelimli programlamaya geçiş için hazırlık niteliğinde örnekleri inceleyeceğiz.
"""

# 1. CLOSURE (KAPANIŞLAR)
# ---------------------
print("1. Closure Örneği:")

def dis_fonksiyon(mesaj):
    def ic_fonksiyon():
        print(f"Mesaj: {mesaj}")  # dis_fonksiyon'un değişkenine erişebilir
    return ic_fonksiyon

# Closure oluşturma
selam = dis_fonksiyon("Merhaba")
selam()  # Mesaj: Merhaba

# 2. DEKORATÖR ZİNCİRLEME
# ---------------------
print("\n2. Dekoratör Zincirleme:")

def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def metin():
    return "Python Programlama"

print(metin())  # <b><i>Python Programlama</i></b>

# 3. PARAMETRE ALAN DEKORATÖRLER
# ---------------------------
print("\n3. Parametre Alan Dekoratörler:")

def tekrar(kac_kez):
    def dekorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(kac_kez):
                sonuc = func(*args, **kwargs)
            return sonuc
        return wrapper
    return dekorator

@tekrar(kac_kez=3)
def mesaj_ver(mesaj):
    print(mesaj)

mesaj_ver("Merhaba!")  # 3 kez yazdırır

# 4. FIRST-CLASS FONKSİYONLAR
# -------------------------
print("\n4. First-Class Fonksiyonlar:")

def islem_yap(func, a, b):
    return func(a, b)

def topla(x, y):
    return x + y

def carp(x, y):
    return x * y

print(f"Toplama: {islem_yap(topla, 5, 3)}")
print(f"Çarpma: {islem_yap(carp, 5, 3)}")

# 5. PARTIAL FONKSİYONLAR
# ---------------------
from functools import partial
print("\n5. Partial Fonksiyonlar:")

def ussu(taban, us):
    return taban ** us

kare = partial(ussu, us=2)
kup = partial(ussu, us=3)

print(f"5'in karesi: {kare(5)}")
print(f"5'in küpü: {kup(5)}")

# 6. GELİŞMİŞ GENERATOR ÖRNEKLER
# ---------------------------
print("\n6. Gelişmiş Generator Örnekler:")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# İlk 10 Fibonacci sayısı
fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")

# 7. CONTEXT MANAGER FONKSİYONLARI
# -----------------------------
from contextlib import contextmanager
print("\n\n7. Context Manager Fonksiyonları:")

@contextmanager
def dosya_yonetimi(dosya_adi, mod):
    try:
        dosya = open(dosya_adi, mod)
        yield dosya
    finally:
        dosya.close()

# Kullanımı:
try:
    with dosya_yonetimi("test.txt", "w") as f:
        f.write("Merhaba, Dünya!")
except FileNotFoundError:
    print("Dosya işlemleri simüle edildi.")

# 8. MEMOIZATION (HAFIZAYA ALMA)
# ---------------------------
print("\n8. Memoization Örneği:")

def memoize(func):
    hafiza = {}
    def wrapper(*args):
        if args not in hafiza:
            hafiza[args] = func(*args)
        return hafiza[args]
    return wrapper

@memoize
def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(f"Fibonacci(10): {fibonacci_recursive(10)}")

"""
İLERİ SEVİYE FONKSİYON KULLANIM İPUÇLARI
---------------------------------------
1. Closure'lar durumu korumak için kullanılır
2. Dekoratörler fonksiyon davranışını değiştirmek için güçlü bir araçtır
3. Generator'lar büyük veri setleri için bellek dostu çözümler sunar
4. Context manager'lar kaynak yönetimi için önemlidir
5. Memoization performans optimizasyonu için kullanılır

NESNE YÖNELİMLİ PROGRAMLAMAYA GEÇİŞ
---------------------------------
1. Fonksiyonlar, metodların temelini oluşturur
2. Closure'lar, sınıf benzeri davranışlar sergiler
3. Dekoratörler, sınıf metodlarını özelleştirmede kullanılır
4. Context manager'lar, nesne yaşam döngüsünü yönetir
5. First-class fonksiyonlar, polimorfizm benzeri davranışlar sağlar

PERFORMANS VE GÜVENLİK
--------------------
1. Memoization ile tekrarlı hesaplamaları önleyin
2. Generator'lar ile bellek kullanımını optimize edin
3. Context manager'lar ile kaynak sızıntılarını önleyin
4. Dekoratör zincirleme kullanımında performansa dikkat edin
5. Recursive fonksiyonlarda memoization kullanmayı düşünün
""" 