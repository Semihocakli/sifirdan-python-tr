"""
Kümeleme Analizi (Clustering Analysis)
---------------------------------
"""

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# Sentetik veri oluştur
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=42)

# Veriyi ölçeklendir
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA uygula
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Farklı kümeleme algoritmalarını uygula
algorithms = {
    'K-Means': KMeans(n_clusters=4, random_state=42),
    'DBSCAN': DBSCAN(eps=0.3, min_samples=5)
}

# Sonuçları görselleştir
plt.figure(figsize=(15, 5))

# Orijinal veri
plt.subplot(131)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title('Orijinal Veri')

# Kümeleme sonuçlarını çiz
for i, (name, algorithm) in enumerate(algorithms.items(), 2):
    # Uydur ve tahmin et
    labels = algorithm.fit_predict(X_scaled)
    
    plt.subplot(1, 3, i)
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    plt.title(f'{name} Kümeleme')

plt.tight_layout()
plt.show()

# Farklı küme sayıları için K-Means'i değerlendir
inertias = []
n_clusters_range = range(1, 11)

for n_clusters in n_clusters_range:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

# Dirsek grafiğini çiz
plt.figure(figsize=(8, 5))
plt.plot(n_clusters_range, inertias, 'bo-')
plt.xlabel('Küme Sayısı')
plt.ylabel('Atalet')
plt.title('Optimal k için Dirsek Yöntemi')
plt.show() 