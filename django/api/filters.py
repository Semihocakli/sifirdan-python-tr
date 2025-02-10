from django_filters import rest_framework as filters
from .models import BlogYazisi

class BlogYazisiFilter(filters.FilterSet):
    baslik = filters.CharFilter(lookup_expr='icontains')
    icerik = filters.CharFilter(lookup_expr='icontains')
    yazar = filters.CharFilter(lookup_expr='iexact')
    tarih_baslangic = filters.DateTimeFilter(field_name='olusturulma_tarihi', lookup_expr='gte')
    tarih_bitis = filters.DateTimeFilter(field_name='olusturulma_tarihi', lookup_expr='lte')

    class Meta:
        model = BlogYazisi
        fields = ['baslik', 'icerik', 'yazar', 'tarih_baslangic', 'tarih_bitis'] 