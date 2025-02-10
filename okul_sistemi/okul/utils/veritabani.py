"""
Veritabanı işlemleri için yardımcı fonksiyonlar.
"""

import sqlite3
from typing import List, Any, Dict
from contextlib import contextmanager

class VeritabaniYoneticisi:
    """Veritabanı işlemlerini yöneten sınıf."""
    
    def __init__(self, db_dosyasi: str = "okul.db"):
        self.db_dosyasi = db_dosyasi
        self.tablolari_olustur()
    
    @contextmanager
    def baglanti_yap(self):
        """Veritabanı bağlantısı oluşturur ve otomatik kapatır."""
        baglanti = sqlite3.connect(self.db_dosyasi)
        baglanti.row_factory = sqlite3.Row  # Dict-like rows
        try:
            yield baglanti
        finally:
            baglanti.close()
    
    def tablolari_olustur(self):
        """Gerekli tabloları oluşturur."""
        with self.baglanti_yap() as baglanti:
            cursor = baglanti.cursor()
            
            # Öğrenci tablosu
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ogrenciler (
                    id INTEGER PRIMARY KEY,
                    ad TEXT NOT NULL,
                    soyad TEXT NOT NULL,
                    ogrenci_no TEXT UNIQUE NOT NULL,
                    dogum_tarihi DATE NOT NULL,
                    sinif INTEGER NOT NULL,
                    devamsizlik INTEGER DEFAULT 0
                )
            """)
            
            # Notlar tablosu
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notlar (
                    id INTEGER PRIMARY KEY,
                    ogrenci_id INTEGER,
                    ders TEXT NOT NULL,
                    puan REAL NOT NULL,
                    FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler (id)
                )
            """)
            
            baglanti.commit()
    
    def kaydet(self, tablo: str, veri: Dict[str, Any]) -> int:
        """Verilen tabloye veri ekler."""
        with self.baglanti_yap() as baglanti:
            cursor = baglanti.cursor()
            
            kolonlar = ", ".join(veri.keys())
            placeholders = ", ".join("?" * len(veri))
            sql = f"INSERT INTO {tablo} ({kolonlar}) VALUES ({placeholders})"
            
            cursor.execute(sql, list(veri.values()))
            baglanti.commit()
            return cursor.lastrowid
    
    def guncelle(self, tablo: str, id: int, veri: Dict[str, Any]) -> None:
        """Verilen ID'ye sahip kaydı günceller."""
        with self.baglanti_yap() as baglanti:
            cursor = baglanti.cursor()
            
            set_clause = ", ".join(f"{k} = ?" for k in veri.keys())
            sql = f"UPDATE {tablo} SET {set_clause} WHERE id = ?"
            
            values = list(veri.values()) + [id]
            cursor.execute(sql, values)
            baglanti.commit()
    
    def sil(self, tablo: str, id: int) -> None:
        """Verilen ID'ye sahip kaydı siler."""
        with self.baglanti_yap() as baglanti:
            cursor = baglanti.cursor()
            cursor.execute(f"DELETE FROM {tablo} WHERE id = ?", (id,))
            baglanti.commit()
    
    def bul(self, tablo: str, id: int) -> Dict[str, Any]:
        """Verilen ID'ye sahip kaydı bulur."""
        with self.baglanti_yap() as baglanti:
            cursor = baglanti.cursor()
            cursor.execute(f"SELECT * FROM {tablo} WHERE id = ?", (id,))
            return dict(cursor.fetchone() or {})
    
    def listele(self, tablo: str, kosul: str = None) -> List[Dict[str, Any]]:
        """Tablodaki kayıtları listeler."""
        with self.baglanti_yap() as baglanti:
            cursor = baglanti.cursor()
            
            sql = f"SELECT * FROM {tablo}"
            if kosul:
                sql += f" WHERE {kosul}"
            
            cursor.execute(sql)
            return [dict(row) for row in cursor.fetchall()]
    
    def ozel_sorgu(self, sql: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """Özel SQL sorgusu çalıştırır."""
        with self.baglanti_yap() as baglanti:
            cursor = baglanti.cursor()
            cursor.execute(sql, params)
            return [dict(row) for row in cursor.fetchall()] 