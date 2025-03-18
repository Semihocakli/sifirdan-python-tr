# ValueError hatası -> Kullanıcıdan alınan değerlerin sayı olup olmadığını kontrol etmek için kullanılır.
# ZeroDivisionError hatası -> Bir sayının sıfıra bölünmesi durumunda oluşur.
# NameError hatası -> Tanımlanmayan bir değişken kullanıldığında oluşur.
# TypeError hatası -> Bir fonksiyonun beklediği tipte bir veri gönderilmediğinde oluşur.
# IndexError hatası -> Bir liste, demet vb. veri tipinde olmayan bir elemanı çağırmaya çalıştığımızda oluşur.
# FileNotFoundError hatası -> Dosya bulunamadığında oluşur.
# ModuleNotFoundError hatası -> Modül bulunamadığında oluşur.
# ImportError hatası -> Bir modül import edilirken hata alındığında oluşur.
# KeyboardInterrupt hatası -> Kullanıcı bir tuşa basarak programın çalışmasını durdurduğunda oluşur.
# MemoryError hatası -> Bellek sınırlarını aştığımızda oluşur.
# OverflowError hatası -> Bir sayının sınırlarını aştığımızda oluşur.
# SyntaxError hatası -> Python dilinde yazım hatası yaptığımızda oluşur.


ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ValueError:
    print("Lütfen sadece sayı girin!")

    """
    try:
        hata verebileceğini bildiğimiz kodlar
    except HataAdı:
        hata durumunda yapılacak işlem
    """

ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ValueError as hata:
    print(hata)