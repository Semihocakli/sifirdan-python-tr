"""
Öğrenci modeli ve ilgili işlemler.
"""

from dataclasses import dataclass
from datetime import date
from typing import List, Dict

@dataclass
class Ogrenci:
    """Öğrenci bilgilerini tutan sınıf."""
    
    id: int
    ad: str
    soyad: str
    ogrenci_no: str
    dogum_tarihi: date
    sinif: int
    notlar: Dict[str, List[float]] = None
    devamsizlik: int = 0
    
    def __post_init__(self):
        """Nesne oluşturulduktan sonra çağrılır."""
        if self.notlar is None:
            self.notlar = {}
    
    def not_ekle(self, ders: str, not_: float) -> None:
        """Öğrenciye not ekler."""
        if not 0 <= not_ <= 100:
            raise ValueError("Not 0-100 arasında olmalıdır!")
        
        if ders not in self.notlar:
            self.notlar[ders] = []
        self.notlar[ders].append(not_)
    
    def ortalama_hesapla(self, ders: str = None) -> float:
        """
        Belirtilen dersin veya tüm derslerin ortalamasını hesaplar.
        
        Args:
            ders: Hesaplanacak ders. None ise tüm dersler hesaplanır.
        
        Returns:
            float: Not ortalaması
        """
        if ders:
            if ders not in self.notlar:
                raise ValueError(f"{ders} dersi bulunamadı!")
            notlar = self.notlar[ders]
        else:
            notlar = [not_ for ders_notlari in self.notlar.values() 
                     for not_ in ders_notlari]
        
        return sum(notlar) / len(notlar) if notlar else 0
    
    def devamsizlik_ekle(self, gun: int = 1) -> None:
        """Öğrenciye devamsızlık ekler."""
        if gun < 0:
            raise ValueError("Devamsızlık günü negatif olamaz!")
        self.devamsizlik += gun
    
    def sinif_atla(self) -> None:
        """Öğrenciyi bir üst sınıfa geçirir."""
        if self.sinif == 12:
            raise ValueError("Öğrenci son sınıfta!")
        self.sinif += 1
    
    def __str__(self) -> str:
        """Öğrenci bilgilerinin string temsili."""
        return f"{self.ad} {self.soyad} ({self.ogrenci_no})"
    
    def bilgi_ver(self) -> str:
        """Öğrencinin detaylı bilgilerini döndürür."""
        return f"""
Öğrenci Bilgileri:
-----------------
Ad Soyad: {self.ad} {self.soyad}
Öğrenci No: {self.ogrenci_no}
Sınıf: {self.sinif}
Doğum Tarihi: {self.dogum_tarihi}
Devamsızlık: {self.devamsizlik} gün
Genel Ortalama: {self.ortalama_hesapla():.2f}
""" 