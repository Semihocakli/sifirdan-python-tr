from django.urls import path
from . import views

urlpatterns = [
    path('merhaba/', views.merhaba_api, name='merhaba-api'),
    path('blog/', views.BlogListesiView.as_view(), name='blog-listesi'),
    path('blog/<int:pk>/', views.BlogDetayView.as_view(), name='blog-detay'),
    path('blog/populer/', views.populer_yazilar, name='populer-yazilar'),
] 