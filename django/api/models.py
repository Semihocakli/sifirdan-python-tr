from django.db import models

# Create your models here.

class BlogYazisi(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    yazar = models.CharField(max_length=100)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog Yazısı'
        verbose_name_plural = 'Blog Yazıları'
        ordering = ['-olusturulma_tarihi']  # En yeni yazılar önce gelsin

    def __str__(self):
        return self.baslik
