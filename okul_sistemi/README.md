# Okul Yönetim Sistemi

Bu proje, Python'da modüler programlama örneği olarak geliştirilmiş basit bir okul yönetim sistemidir.

## Proje Yapısı

```
okul_sistemi/
│
├── README.md           # Proje dokümantasyonu
├── requirements.txt    # Proje bağımlılıkları
│
├── okul/              # Ana paket dizini
│   ├── __init__.py    # Paket tanımlayıcı
│   │
│   ├── modeller/      # Veri modelleri
│   │   ├── __init__.py
│   │   ├── ogrenci.py
│   │   ├── ogretmen.py
│   │   └── ders.py
│   │
│   ├── utils/         # Yardımcı fonksiyonlar
│   │   ├── __init__.py
│   │   ├── veritabani.py
│   │   └── dogrulama.py
│   │
│   └── arayuz/        # Kullanıcı arayüzü
│       ├── __init__.py
│       └── menu.py
│
└── test/              # Test dosyaları
    ├── __init__.py
    └── test_ogrenci.py

```

## Kullanım

1. Sanal ortam oluşturun:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

3. Uygulamayı çalıştırın:
```bash
python -m okul.arayuz.menu
```

## Özellikler

- Öğrenci kaydı ve yönetimi
- Öğretmen kaydı ve yönetimi
- Ders programı oluşturma
- Not takibi
- Devamsızlık takibi

## Geliştirici Notları

- Her modül tek bir sorumluluğa sahiptir
- Modüller arası bağımlılıklar minimize edilmiştir
- PEP 8 standartlarına uyulmuştur
- Kapsamlı hata yönetimi eklenmiştir

## Modülleri Kullanma

Okul sistemindeki modülleri kullanmak için aşağıdaki örnekleri inceleyebilirsiniz:

### 1. Temel Import İşlemleri

Import işlemi, başka Python dosyalarındaki kodları kullanmamızı sağlar. Yani başka dosyalardaki hazır kodları kendi programımıza dahil edebiliriz.

```python
# Tüm modülleri tek seferde import etme
from okul.modeller import Ogrenci, Ogretmen, Ders

# Ya da tek tek import etme
from okul.modeller.ogrenci import Ogrenci
from okul.modeller.ogretmen import Ogretmen
from okul.modeller.ders import Ders

# Veritabanı yöneticisini import etme
from okul.utils.veritabani import VeritabaniYoneticisi
```

### 2. Örnek Kullanımlar

Aşağıdaki örnekler, modülleri nasıl kullanacağınızı gösterir:

```python
# Öğrenci oluşturma
ogrenci = Ogrenci(
    id=1,                    # Öğrenci numarası
    ad="Ahmet",             # Öğrencinin adı
    soyad="Yılmaz",         # Öğrencinin soyadı
    ogrenci_no="2023001",   # Okul numarası
    dogum_tarihi="2005-01-15", # Doğum tarihi
    sinif=10                # Sınıfı
)

# Öğretmen oluşturma
ogretmen = Ogretmen(
    id=1,
    ad="Ayşe",
    soyad="Demir",
    sicil_no="12345",         # Öğretmen sicil numarası
    brans="Matematik",        # Branşı
    giris_tarihi="2020-09-01" # İşe başlama tarihi
)

# Ders oluşturma
ders = Ders(
    id=1,
    ad="Matematik",          # Dersin adı
    kod="MAT101",           # Ders kodu
    kredi=4,                # Ders kredisi
    ogretmen_id=1           # Dersi veren öğretmenin ID'si
)

# Veritabanı işlemleri
db = VeritabaniYoneticisi()  # Veritabanı bağlantısı oluştur
db.kaydet("ogrenciler", {    # Öğrenci bilgilerini kaydet
    "ad": "Ahmet",
    "soyad": "Yılmaz",
    "ogrenci_no": "2023001",
    "dogum_tarihi": "2005-01-15",
    "sinif": 10
})
```

### Önemli Notlar

1. Import işlemlerini dosyanın en başında yapın
2. Her modül belirli bir işlevi yerine getirir:
   - `ogrenci.py`: Öğrenci işlemleri
   - `ogretmen.py`: Öğretmen işlemleri
   - `ders.py`: Ders işlemleri
   - `veritabani.py`: Veritabanı işlemleri
3. Modülleri kullanmadan önce projenin ana dizininde olduğunuzdan emin olun
4. Hata mesajlarını dikkatlice okuyun, genellikle import hatalarının çözümünü gösterirler
