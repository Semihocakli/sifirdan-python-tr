# Python'da Veritabanı İşlemleri (SQLite)
# ================================

"""
VERİTABANI İŞLEMLERİ NEDİR?
-------------------------
Veritabanı işlemleri, verilerinizi:
1. Kalıcı olarak saklama
2. Organize etme
3. Sorgulama
4. Güncelleme
5. Silme
gibi işlemleri yapmanızı sağlar.

SQLite:
- Python'un standart kütüphanesinde bulunur
- Sunucu gerektirmez
- Tek bir dosyada çalışır
- Küçük ve orta ölçekli uygulamalar için idealdir
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Any

# 1. VERİTABANI BAĞLANTISI
# ----------------------
print("1. Veritabanı Bağlantısı:")

def veritabani_baglantisi(db_dosyasi: str = "okul.db") -> sqlite3.Connection:
    """Veritabanı bağlantısı oluşturur."""
    try:
        baglanti = sqlite3.connect(db_dosyasi)
        print(f"{db_dosyasi} veritabanına bağlantı başarılı!")
        return baglanti
    except sqlite3.Error as e:
        print(f"Bağlantı hatası: {e}")
        raise

# 2. TABLO OLUŞTURMA
# ----------------
print("\n2. Tablo Oluşturma:")

def tablolari_olustur(baglanti: sqlite3.Connection) -> None:
    """Gerekli tabloları oluşturur."""
    try:
        cursor = baglanti.cursor()
        
        # Öğrenciler tablosu
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ogrenciler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ad TEXT NOT NULL,
                soyad TEXT NOT NULL,
                numara TEXT UNIQUE NOT NULL,
                dogum_tarihi DATE,
                kayit_tarihi DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Dersler tablosu
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dersler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                kod TEXT UNIQUE NOT NULL,
                ad TEXT NOT NULL,
                kredi INTEGER NOT NULL
            )
        """)
        
        # Notlar tablosu
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notlar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ogrenci_id INTEGER,
                ders_id INTEGER,
                not_degeri REAL NOT NULL,
                tarih DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler (id),
                FOREIGN KEY (ders_id) REFERENCES dersler (id)
            )
        """)
        
        baglanti.commit()
        print("Tablolar başarıyla oluşturuldu!")
        
    except sqlite3.Error as e:
        print(f"Tablo oluşturma hatası: {e}")
        baglanti.rollback()

# 3. VERİ EKLEME
# ------------
print("\n3. Veri Ekleme:")

def ogrenci_ekle(baglanti: sqlite3.Connection, ad: str, soyad: str, 
                numara: str, dogum_tarihi: str) -> int:
    """Yeni öğrenci ekler ve eklenen öğrencinin ID'sini döndürür."""
    try:
        cursor = baglanti.cursor()
        cursor.execute("""
            INSERT INTO ogrenciler (ad, soyad, numara, dogum_tarihi)
            VALUES (?, ?, ?, ?)
        """, (ad, soyad, numara, dogum_tarihi))
        
        baglanti.commit()
        print(f"Öğrenci eklendi! ID: {cursor.lastrowid}")
        return cursor.lastrowid
        
    except sqlite3.IntegrityError:
        print(f"Hata: {numara} numaralı öğrenci zaten mevcut!")
        return -1
    except sqlite3.Error as e:
        print(f"Veri ekleme hatası: {e}")
        baglanti.rollback()
        return -1

# 4. VERİ SORGULAMA
# ---------------
print("\n4. Veri Sorgulama:")

def ogrenci_bul(baglanti: sqlite3.Connection, numara: str = None) -> List[Dict[str, Any]]:
    """Öğrenci bilgilerini sorgular."""
    try:
        cursor = baglanti.cursor()
        if numara:
            cursor.execute("""
                SELECT * FROM ogrenciler WHERE numara = ?
            """, (numara,))
        else:
            cursor.execute("SELECT * FROM ogrenciler")
        
        # Sütun isimlerini al
        kolonlar = [description[0] for description in cursor.description]
        
        # Sonuçları sözlük listesi olarak döndür
        sonuclar = []
        for row in cursor.fetchall():
            sonuclar.append(dict(zip(kolonlar, row)))
        
        return sonuclar
        
    except sqlite3.Error as e:
        print(f"Sorgulama hatası: {e}")
        return []

# 5. VERİ GÜNCELLEME
# ----------------
print("\n5. Veri Güncelleme:")

def ogrenci_guncelle(baglanti: sqlite3.Connection, numara: str, 
                     yeni_bilgiler: Dict[str, Any]) -> bool:
    """Öğrenci bilgilerini günceller."""
    try:
        cursor = baglanti.cursor()
        
        # Güncellenecek alanları ve değerleri hazırla
        set_clause = ", ".join(f"{k} = ?" for k in yeni_bilgiler.keys())
        values = list(yeni_bilgiler.values()) + [numara]
        
        cursor.execute(f"""
            UPDATE ogrenciler
            SET {set_clause}
            WHERE numara = ?
        """, values)
        
        baglanti.commit()
        print(f"Öğrenci güncellendi! Etkilenen kayıt: {cursor.rowcount}")
        return cursor.rowcount > 0
        
    except sqlite3.Error as e:
        print(f"Güncelleme hatası: {e}")
        baglanti.rollback()
        return False

# 6. VERİ SİLME
# -----------
print("\n6. Veri Silme:")

def ogrenci_sil(baglanti: sqlite3.Connection, numara: str) -> bool:
    """Öğrenci kaydını siler."""
    try:
        cursor = baglanti.cursor()
        cursor.execute("DELETE FROM ogrenciler WHERE numara = ?", (numara,))
        
        baglanti.commit()
        print(f"Öğrenci silindi! Etkilenen kayıt: {cursor.rowcount}")
        return cursor.rowcount > 0
        
    except sqlite3.Error as e:
        print(f"Silme hatası: {e}")
        baglanti.rollback()
        return False

# 7. ÖRNEK KULLANIM
# --------------
print("\n7. Örnek Kullanım:")

def ornek_kullanim():
    """Veritabanı işlemlerinin örnek kullanımı."""
    try:
        # Veritabanı bağlantısı
        baglanti = veritabani_baglantisi()
        
        # Tabloları oluştur
        tablolari_olustur(baglanti)
        
        # Örnek öğrenci ekle
        ogrenci_id = ogrenci_ekle(
            baglanti,
            "Ahmet",
            "Yılmaz",
            "2023001",
            "2005-01-15"
        )
        
        # Tüm öğrencileri listele
        print("\nTüm öğrenciler:")
        ogrenciler = ogrenci_bul(baglanti)
        for ogrenci in ogrenciler:
            print(ogrenci)
        
        # Öğrenci güncelle
        guncelleme = {
            "ad": "Mehmet",
            "soyad": "Yılmaz"
        }
        ogrenci_guncelle(baglanti, "2023001", guncelleme)
        
        # Güncellenmiş öğrenciyi göster
        print("\nGüncellenmiş öğrenci:")
        print(ogrenci_bul(baglanti, "2023001"))
        
        # Öğrenciyi sil
        ogrenci_sil(baglanti, "2023001")
        
        baglanti.close()
        print("\nVeritabanı bağlantısı kapatıldı!")
        
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    ornek_kullanim()

"""
VERİTABANI İŞLEMLERİ İPUÇLARI
--------------------------
1. Bağlantıları her zaman kapatın
2. Hata yönetimi ekleyin
3. Parametreli sorgular kullanın (SQL Injection'a karşı)
4. Transaction'ları doğru yönetin
5. Bağlantı havuzu kullanmayı düşünün

GÜVENLİK ÖNLEMLERİ
----------------
1. SQL Injection'a karşı önlem alın
2. Kullanıcı girişlerini doğrulayın
3. Yetkilendirme kontrolleri ekleyin
4. Hassas verileri şifreleyin
5. Veritabanı dosyasını koruyun

PERFORMANS İPUÇLARI
----------------
1. İndeksler kullanın
2. Sorguları optimize edin
3. Büyük veri setlerini sayfalayın
4. Connection pooling kullanın
5. Gereksiz sorguları minimize edin
""" 