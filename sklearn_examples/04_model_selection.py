"""
Model Seçimi ve Değerlendirme (Model Selection)
-----------------------------------------
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükle
data = load_breast_cancer()
X, y = data.data, data.target

# İşlem hatlarını oluştur
pipelines = {
    'svm': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SVC())
    ]),
    'rf': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier())
    ])
}

# GridSearchCV için parametre ızgaraları
param_grids = {
    'svm': {
        'classifier__C': [0.1, 1, 10],
        'classifier__kernel': ['linear', 'rbf']
    },
    'rf': {
        'classifier__n_estimators': [100, 200],
        'classifier__max_depth': [None, 10, 20]
    }
}

# Her işlem hattı için GridSearchCV uygula
results = {}
for name, pipeline in pipelines.items():
    grid_search = GridSearchCV(
        pipeline, 
        param_grids[name], 
        cv=5, 
        scoring='accuracy',
        n_jobs=-1
    )
    grid_search.fit(X, y)
    
    results[name] = {
        'best_params': grid_search.best_params_,
        'best_score': grid_search.best_score_,
        'cv_results': grid_search.cv_results_
    }
    
    print(f"\n{name.upper()} Sonuçları:")
    print(f"En iyi parametreler: {grid_search.best_params_}")
    print(f"En iyi çapraz doğrulama skoru: {grid_search.best_score_:.3f}")

# Çapraz doğrulama sonuçlarını görselleştir
plt.figure(figsize=(12, 5))

for i, (name, result) in enumerate(results.items(), 1):
    plt.subplot(1, 2, i)
    
    # Farklı parametreler için skorları çıkar
    scores = np.array(result['cv_results_']['mean_test_score'])
    scores = scores.reshape(len(param_grids[name][list(param_grids[name].keys())[0]]), -1)
    
    sns.heatmap(scores, annot=True, fmt='.3f', cmap='YlOrRd')
    plt.title(f'{name.upper()} Çapraz Doğrulama Skorları')
    
    # Parametrelere göre etiketleri ayarla
    param_names = list(param_grids[name].keys())
    plt.xlabel(param_names[1].split('__')[1])
    plt.ylabel(param_names[0].split('__')[1])

plt.tight_layout()
plt.show() 