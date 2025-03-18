#https://python-istihza.yazbel.com/standart_moduller/sqlite.html
'''
1.) sqlite3 modülünü projenize dahil edin
2.) Mevcut veya yeni veritabanınızı connect() fonksiyonu ile bağlayın
3.) cursor() fonksiyonu ile imleç oluşturun
4.) Sql komutlarınızı execute() fonksiyonu ile işletin.
5.) Veritabanınızda değişiklik olacaksa commit() edin.
6.) Veritabanı bağlantınızı close() ile sonlandırın.

'''

'''
import sqlite3 as sql

vt = sql.connect('kitaplik.sqlite')
imlec = vt.cursor()
try:
    imlec.execute('CREATE TABLE IF NOT EXISTS kitap_bilgisi (kitap_adi,kitap_yazari, okunma_durumu,begeni)')
except:
    print("tablo zaten vardı oluşturmadı")

kitap_girisi = "INSERT INTO kitap_bilgisi VALUES ('Suç ve Ceza', 'Dostoyevski', 'hayır','*****')" #1.yöntem
imlec.execute(kitap_girisi)

imlec.execute("INSERT INTO kitap_bilgisi VALUES ('Beyaz Diş', 'Jack LONDON', 'evet','***')") # 2.yöntem

imlec.execute("INSERT INTO kitap_bilgisi VALUES ('Kinyas ve Kayra', 'Hakan Günday', 'evet','*****')")

imlec.execute("INSERT INTO kitap_bilgisi VALUES ('Yunan Mitolojisi', 'Anna', 'hayır','****')")
vt.commit()

vt.close()

vt = sql.connect('kitaplik.sqlite')
imlec = vt.cursor()

imlec.execute("SELECT * FROM kitap_bilgisi")
veriler = imlec.fetchall()

for veri in veriler:
    print(veri)

vt.close()


import sqlite3

with sqlite3.connect('vt.sqlite') as vt:
    im = vt.cursor()

    veriler = [('Fırat', 'Özgül', 'Adana'),
               ('Ahmet', 'Söz', 'Bolvadin'),
               ('Veli', 'Göz', 'İskenderun'),
               ('Mehmet', 'Öz', 'Kilis')]

    im.execute("""CREATE TABLE IF NOT EXISTS personel
        (isim, soyisim, memleket)""")

    for veri in veriler:
        im.execute("""INSERT INTO personel VALUES
            (?, ?, ?)""", veri)

    vt.commit()
'''

import sqlite3

#vt.sqlite adlı bir veritabanı dosyası oluşturup
#bu veritabanına bağlanıyoruz.
db = sqlite3.connect("vt.sqlite")

#Veritabanı üzerinde istediğimiz işlemleri yapabilmek
#için bir imleç oluşturmamız gerekiyor.
im = db.cursor()

#imlecin execute() metodunu kullanarak, veritabanı içinde
#"kullanicilar" adlı bir tablo oluşturuyoruz. Bu tabloda
#kullanıcı_adi ve parola olmak üzere iki farklı sütun var.
im.execute("""CREATE TABLE IF NOT EXISTS kullanicilar
    (kullanici_adi, parola)""")

#Yukarıda oluşturduğumuz tabloya yerleştireceğimiz verileri
#hazırlıyoruz. Verilerin liste içinde birer demet olarak
#nasıl gösterildiğine özellikle dikkat ediyoruz.
veriler = [
            ("ahmet123", "12345678"),
            ("mehmet321", "87654321"),
            ("selin456", "123123123")
          ]

#veriler adlı liste içindeki bütün verileri kullanicilar adlı
#tabloya yerleştiriyoruz. Burada tek öğeli bir demet
#tanımladığımıza dikkat edin: (i,)
for i in veriler:
    im.execute("""INSERT INTO kullanicilar VALUES %s""" %(i,))

#Yaptığımız değişikliklerin tabloya işlenebilmesi için
#commit() metodunu kullanıyoruz.
db.commit()

#Kullanıcıdan kullanıcı adı ve parola bilgilerini alıyoruz...
kull = input("Kullanıcı adınız: ")
paro = input("Parolanız: ")

#Burada yine bir SQL komutu işletiyoruz. Bu komut, kullanicilar
#adlı tabloda yer alan kullanici_adi ve parola adlı sütunlardaki
#bilgileri seçiyor.
im.execute("""SELECT * FROM kullanicilar WHERE
kullanici_adi = '%s' AND parola = '%s'"""%(kull, paro))

#Hatırlarsanız daha önce fetchall() adlı bir metottan
#söz etmiştik. İşte bu fetchone() metodu da ona benzer.
#fetchall() bütün verileri alıyordu, fetchone() ise
#verileri tek tek alır.
data = im.fetchone()

#Eğer data adlı değişken False değilse, yani bu
#değişkenin içinde bir değer varsa kullanıcı adı
#ve parola doğru demektir. Kullanıcıyı içeri alıyoruz.
if data:
    print("Programa hoşgeldin {}!".format(data[0]))

#Aksi halde kullanıcıya olumsuz bir mesaj veriyoruz.
else:
    print("Parola veya kullanıcı adı yanlış!")