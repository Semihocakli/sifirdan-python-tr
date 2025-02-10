"""
Kullanıcı arayüzü için menü sistemi.
"""

import os
import sys
from datetime import datetime
from typing import Callable, Dict

# Ana dizini Python path'ine ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from okul.utils.veritabani import VeritabaniYoneticisi

class Menu:
    """Ana menü sınıfı."""
    
    def __init__(self):
        self.db = VeritabaniYoneticisi()
        self.secenekler: Dict[str, Callable] = {
            "1": self.ogrenci_ekle,
            "2": self.ogrenci_listele,
            "3": self.not_ekle,
            "4": self.devamsizlik_ekle,
            "5": self.ogrenci_bilgi,
            "q": self.cikis
        }
    
    def ana_menu(self) -> None:
        """Ana menüyü gösterir ve kullanıcı seçimini işler."""
        while True:
            self.menu_goster()
            secim = input("\nSeçiminiz: ").lower()
            
            if secim in self.secenekler:
                self.secenekler[secim]()
                if secim == "q":
                    break
            else:
                print("Geçersiz seçim!")
            
            input("\nDevam etmek için Enter'a basın...")
    
    def menu_goster(self) -> None:
        """Menü seçeneklerini gösterir."""
        print("""
╔════════════════════════════╗
║     OKUL YÖNETİM SİSTEMİ  ║
╠════════════════════════════╣
║ 1. Öğrenci Ekle           ║
║ 2. Öğrencileri Listele    ║
║ 3. Not Ekle               ║
║ 4. Devamsızlık Ekle       ║
║ 5. Öğrenci Bilgi Görüntüle║
║ Q. Çıkış                  ║
╚════════════════════════════╝
""")
    
    def ogrenci_ekle(self) -> None:
        """Yeni öğrenci ekler."""
        print("\nÖğrenci Ekleme")
        print("-" * 20)
        
        try:
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            ogrenci_no = input("Öğrenci No: ")
            dogum_tarihi = input("Doğum Tarihi (YYYY-MM-DD): ")
            sinif = int(input("Sınıf: "))
            
            # Veri doğrulama
            if not all([ad, soyad, ogrenci_no, dogum_tarihi]):
                raise ValueError("Tüm alanlar doldurulmalıdır!")
            
            if not 1 <= sinif <= 12:
                raise ValueError("Geçersiz sınıf!")
            
            # Veritabanına kaydet
            ogrenci_data = {
                "ad": ad,
                "soyad": soyad,
                "ogrenci_no": ogrenci_no,
                "dogum_tarihi": dogum_tarihi,
                "sinif": sinif,
                "devamsizlik": 0
            }
            
            self.db.kaydet("ogrenciler", ogrenci_data)
            print("\nÖğrenci başarıyla eklendi!")
            
        except ValueError as e:
            print(f"\nHata: {e}")
        except Exception as e:
            print(f"\nBeklenmeyen hata: {e}")
    
    def ogrenci_listele(self) -> None:
        """Tüm öğrencileri listeler."""
        print("\nÖğrenci Listesi")
        print("-" * 50)
        
        ogrenciler = self.db.listele("ogrenciler")
        
        if not ogrenciler:
            print("Kayıtlı öğrenci yok!")
            return
        
        print(f"{'ID':<5} {'Ad':<15} {'Soyad':<15} {'Öğrenci No':<10} {'Sınıf':<5}")
        print("-" * 50)
        
        for ogr in ogrenciler:
            print(f"{ogr['id']:<5} {ogr['ad']:<15} {ogr['soyad']:<15} "
                  f"{ogr['ogrenci_no']:<10} {ogr['sinif']:<5}")
    
    def not_ekle(self) -> None:
        """Öğrenciye not ekler."""
        try:
            ogrenci_no = input("\nÖğrenci No: ")
            ders = input("Ders: ")
            puan = float(input("Not: "))
            
            # Öğrenciyi bul
            ogrenci = self.db.listele("ogrenciler", f"ogrenci_no = '{ogrenci_no}'")
            if not ogrenci:
                raise ValueError("Öğrenci bulunamadı!")
            
            # Not ekle
            not_data = {
                "ogrenci_id": ogrenci[0]["id"],
                "ders": ders,
                "puan": puan
            }
            
            self.db.kaydet("notlar", not_data)
            print("\nNot başarıyla eklendi!")
            
        except ValueError as e:
            print(f"\nHata: {e}")
        except Exception as e:
            print(f"\nBeklenmeyen hata: {e}")
    
    def devamsizlik_ekle(self) -> None:
        """Öğrenciye devamsızlık ekler."""
        try:
            ogrenci_no = input("\nÖğrenci No: ")
            gun = int(input("Gün sayısı: "))
            
            # Öğrenciyi bul
            ogrenci = self.db.listele("ogrenciler", f"ogrenci_no = '{ogrenci_no}'")
            if not ogrenci:
                raise ValueError("Öğrenci bulunamadı!")
            
            # Devamsızlık güncelle
            yeni_devamsizlik = ogrenci[0]["devamsizlik"] + gun
            self.db.guncelle("ogrenciler", ogrenci[0]["id"], 
                           {"devamsizlik": yeni_devamsizlik})
            
            print("\nDevamsızlık başarıyla eklendi!")
            
        except ValueError as e:
            print(f"\nHata: {e}")
        except Exception as e:
            print(f"\nBeklenmeyen hata: {e}")
    
    def ogrenci_bilgi(self) -> None:
        """Öğrenci bilgilerini görüntüler."""
        try:
            ogrenci_no = input("\nÖğrenci No: ")
            
            # Öğrenciyi bul
            ogrenci = self.db.listele("ogrenciler", f"ogrenci_no = '{ogrenci_no}'")
            if not ogrenci:
                raise ValueError("Öğrenci bulunamadı!")
            
            ogr = ogrenci[0]
            
            # Notları al
            notlar = self.db.listele("notlar", f"ogrenci_id = {ogr['id']}")
            
            # Bilgileri göster
            print(f"""
Öğrenci Bilgileri:
-----------------
Ad Soyad: {ogr['ad']} {ogr['soyad']}
Öğrenci No: {ogr['ogrenci_no']}
Sınıf: {ogr['sinif']}
Doğum Tarihi: {ogr['dogum_tarihi']}
Devamsızlık: {ogr['devamsizlik']} gün

Notlar:
-------""")
            
            if notlar:
                for not_ in notlar:
                    print(f"{not_['ders']}: {not_['puan']}")
            else:
                print("Henüz not girilmemiş!")
            
        except ValueError as e:
            print(f"\nHata: {e}")
        except Exception as e:
            print(f"\nBeklenmeyen hata: {e}")
    
    def cikis(self) -> None:
        """Programdan çıkış yapar."""
        print("\nProgramdan çıkılıyor...")

if __name__ == "__main__":
    menu = Menu()
    menu.ana_menu() 