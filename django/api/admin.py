from django.contrib import admin
from .models import BlogYazisi

@admin.register(BlogYazisi)
class BlogYazisiAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'yazar', 'olusturulma_tarihi', 'guncelleme_tarihi')
    list_filter = ('yazar', 'olusturulma_tarihi')
    search_fields = ('baslik', 'icerik', 'yazar')
