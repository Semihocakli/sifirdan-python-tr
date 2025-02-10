"""
Ders modeli ve ilgili işlemler.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class Ders:
    """Ders bilgilerini tutan sınıf."""
    
    id: int
    ad: str
    kod: str
    kredi: int
    ogretmen_id: int = None
    ogrenci_listesi: List[int] = None
    
    def __post_init__(self):
        if self.ogrenci_listesi is None:
            self.ogrenci_listesi = []
    
    def __str__(self) -> str:
        return f"{self.ad} ({self.kod})" 