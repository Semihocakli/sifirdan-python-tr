"""
Okul Yönetim Sistemi
-------------------
Bu paket, okul yönetim sisteminin temel fonksiyonlarını içerir.
"""

__version__ = "1.0.0"
__author__ = "Python Kursu"

# Alt modülleri dışa aç
from . import modeller
from . import utils
from . import arayuz

# Sık kullanılan sınıfları doğrudan erişilebilir yap
from .modeller.ogrenci import Ogrenci
from .modeller.ogretmen import Ogretmen
from .modeller.ders import Ders 