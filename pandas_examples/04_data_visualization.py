"""
Pandas Veri Görselleştirme
------------------------
Bu örnek, Pandas ve Matplotlib kullanarak veri görselleştirme işlemlerini gösterir.
Çizgi grafikleri, sütun grafikleri ve dağılım grafikleri gibi temel grafik türlerini içerir.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Türkçe karakter desteği için
plt.rcParams['font.family'] = 'DejaVu Sans'

# Örnek veri seti oluştur
tarihler = pd.date_range('2023-01-01', periods=12, freq='M')
veri = pd.DataFrame({
    'aylar': tarihler,
    'satis': np.random.randint(100, 200, 12),
    'maliyet': np.random.randint(50, 100, 12),
    'kar': np.random.randint(30, 80, 12)
})

# Çizgi grafiği
plt.figure(figsize=(10, 6))
plt.plot(veri['aylar'], veri['satis'], label='Satış')
plt.plot(veri['aylar'], veri['maliyet'], label='Maliyet')
plt.plot(veri['aylar'], veri['kar'], label='Kâr')
plt.title('Aylık Satış, Maliyet ve Kâr Trendi')
plt.xlabel('Aylar')
plt.ylabel('Miktar (TL)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Sütun grafiği
plt.figure(figsize=(10, 6))
veri[['satis', 'maliyet', 'kar']].mean().plot(kind='bar')
plt.title('Ortalama Satış, Maliyet ve Kâr')
plt.xlabel('Kategoriler')
plt.ylabel('Ortalama Miktar (TL)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Kutu grafiği (Box Plot)
plt.figure(figsize=(10, 6))
veri.boxplot(column=['satis', 'maliyet', 'kar'])
plt.title('Satış, Maliyet ve Kâr Dağılımı')
plt.ylabel('Miktar (TL)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Dağılım grafiği (Scatter Plot)
plt.figure(figsize=(10, 6))
plt.scatter(veri['maliyet'], veri['kar'], alpha=0.5)
plt.title('Maliyet ve Kâr İlişkisi')
plt.xlabel('Maliyet (TL)')
plt.ylabel('Kâr (TL)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Pasta grafiği
plt.figure(figsize=(8, 8))
veri[['satis', 'maliyet', 'kar']].mean().plot(kind='pie', autopct='%1.1f%%')
plt.title('Satış, Maliyet ve Kâr Dağılımı (Yüzde)')
plt.axis('equal')
plt.tight_layout()
plt.show() 