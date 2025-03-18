import sqlite3 as sql
import random

def create_database():
    conn = sql.connect('sansliüclü.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sansliüclü (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT,
            soyad TEXT,
            sayilar TEXT,
            sayi INTEGER       
        )
    ''')
    conn.commit()
    conn.close()

def kullanici_ekle(ad, soyad, sayilar, rastgele_sayi):
    conn = sql.connect('sansliüclü.sqlite')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sansliüclü (ad, soyad, sayilar, sayi) VALUES (?, ?, ?, ?)', (ad, soyad, sayilar, rastgele_sayi))
    conn.commit()
    conn.close()

def main():
    create_database()
    try:
        while True:
            ad = input("Adınızı girin: ")
            soyad = input("Soyadınızı girin: ")
            sayilar = input("(100-200 arası) 3 Basamaklı sayı girin: ")
            rastgele_sayi = random.randint(100, 200)
            
            kullanici_ekle(ad, soyad, sayilar, rastgele_sayi)
            print("Kullanıcı bilgileri veritabanına kaydedildi.")
            
            devam = input("Başka bir kullanıcı eklemek istiyor musunuz? (E/H): ").strip().lower()
            if devam != 'e':
                break
    except KeyboardInterrupt:
        print("\nİşlem sona erdi.")
        

if __name__ == "__main__":
    main()
