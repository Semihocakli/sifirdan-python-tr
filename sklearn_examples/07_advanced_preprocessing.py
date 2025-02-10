"""
Gelişmiş Ön İşleme (Advanced Preprocessing)
-------------------------------------
"""

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Örnek veri seti oluştur
np.random.seed(42)
n_samples = 1000

# Karışık veri tipleri ve eksik değerler içeren DataFrame oluştur
data = {
    'sayisal_1': np.random.normal(0, 1, n_samples),
    'sayisal_2': np.random.normal(10, 5, n_samples),
    'kategori_1': np.random.choice(['A', 'B', 'C'], n_samples),
    'kategori_2': np.random.choice(['X', 'Y', 'Z'], n_samples),
    'sıralı': np.random.choice(['Düşük', 'Orta', 'Yüksek'], n_samples),
    'ikili': np.random.choice([0, 1], n_samples)
}

df = pd.DataFrame(data)

# Eksik değerler ekle
for col in df.columns:
    mask = np.random.random(n_samples) < 0.1
    df.loc[mask, col] = np.nan

# Özellik tiplerini tanımla
sayisal_ozellikler = ['sayisal_1', 'sayisal_2']
kategorik_ozellikler = ['kategori_1', 'kategori_2']
sirali_ozellikler = ['sıralı']
ikili_ozellikler = ['ikili']

# Ön işleme işlem hatlarını oluştur
sayisal_donusturucu = Pipeline(steps=[
    ('doldurma', KNNImputer(n_neighbors=5)),
    ('olcekleme', StandardScaler())
])

kategorik_donusturucu = Pipeline(steps=[
    ('doldurma', SimpleImputer(strategy='constant', fill_value='eksik')),
    ('onehot', OneHotEncoder(drop='first', sparse=False))
])

sirali_donusturucu = Pipeline(steps=[
    ('doldurma', SimpleImputer(strategy='constant', fill_value='Orta')),
    ('kodlayici', LabelEncoder())
])

# Tüm dönüştürücüleri birleştir
onislemci = ColumnTransformer(
    transformers=[
        ('sayisal', sayisal_donusturucu, sayisal_ozellikler),
        ('kategorik', kategorik_donusturucu, kategorik_ozellikler),
        ('sirali', sirali_donusturucu, sirali_ozellikler)
    ])

# Tam işlem hattını oluştur
islem_hatti = Pipeline([
    ('onislemci', onislemci),
    ('siniflandirici', RandomForestClassifier())
])

# Veriyi böl
X = df.drop('ikili', axis=1)
y = df['ikili']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# İşlem hattını eğit ve değerlendir
islem_hatti.fit(X_train, y_train)
skor = islem_hatti.score(X_test, y_test)
print(f"Model doğruluğu: {skor:.4f}")

# Ön işleme etkilerini görselleştir
plt.figure(figsize=(15, 5))

# Orijinal sayısal dağılım
plt.subplot(131)
sns.histplot(df['sayisal_1'].dropna(), bins=30)
plt.title('Orijinal Dağılım')

# Ölçeklenmiş sayısal dağılım
olceklenmis_veri = islem_hatti.named_steps['onislemci'].transform(X_train)
plt.subplot(132)
sns.histplot(olceklenmis_veri[:, 0], bins=30)
plt.title('Ölçeklenmiş Dağılım')

# Eksik değerlerin gösterimi
plt.subplot(133)
eksik_sayilar = df.isnull().sum()
sns.barplot(x=eksik_sayilar.index, y=eksik_sayilar.values)
plt.xticks(rotation=45)
plt.title('Özelliklere Göre Eksik Değerler')

plt.tight_layout()
plt.show() 