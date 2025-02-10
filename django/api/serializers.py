from rest_framework import serializers
from .models import BlogYazisi

class BlogYazisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogYazisi
        fields = ['id', 'baslik', 'icerik', 'yazar', 'olusturulma_tarihi', 'guncelleme_tarihi']
        read_only_fields = ['olusturulma_tarihi', 'guncelleme_tarihi'] 