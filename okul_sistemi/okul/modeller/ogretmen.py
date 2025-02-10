"""
Öğretmen modeli ve ilgili işlemler.
"""

from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass
class Ogretmen:
    """Öğretmen bilgilerini tutan sınıf."""
    
    id: int
    ad: str
    soyad: str
    sicil_no: str
    brans: str
    giris_tarihi: date
    dersler: List[str] = None
    
    def __post_init__(self):
        """Nesne oluşturulduktan sonra çağrılır."""
        if self.dersler is None:
            self.dersler = []
    
    def ders_ekle(self, ders: str) -> None:
        """Öğretmene ders ekler."""
        if ders not in self.dersler:
            self.dersler.append(ders)
    
    def __str__(self) -> str:
        """Öğretmen bilgilerinin string temsili."""
        return f"{self.ad} {self.soyad} ({self.brans})" 