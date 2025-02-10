from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from django.utils import timezone
from datetime import timedelta
from .models import BlogYazisi
from .serializers import BlogYazisiSerializer
from .permissions import IsYazarOrReadOnly
from .filters import BlogYazisiFilter

# Create your views here.

@api_view(['GET'])
def merhaba_api(request):
    return Response({
        'mesaj': 'Merhaba! İlk Django REST API endpoint\'iniz başarıyla çalışıyor.',
        'yapimci': 'Django REST Framework',
        'versiyon': '1.0'
    })

@api_view(['GET'])
def populer_yazilar(request):
    """Son 7 günün en popüler yazılarını listeler"""
    bir_hafta_once = timezone.now() - timedelta(days=7)
    yazilar = BlogYazisi.objects.filter(
        olusturulma_tarihi__gte=bir_hafta_once
    ).order_by('-olusturulma_tarihi')[:5]
    
    serializer = BlogYazisiSerializer(yazilar, many=True)
    return Response({
        'mesaj': 'Son 7 günün en popüler yazıları',
        'yazilar': serializer.data
    })

class BlogListesiView(generics.ListCreateAPIView):
    queryset = BlogYazisi.objects.all()
    serializer_class = BlogYazisiSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = BlogYazisiFilter
    search_fields = ['baslik', 'icerik', 'yazar']
    ordering_fields = ['olusturulma_tarihi', 'guncelleme_tarihi', 'baslik']
    ordering = ['-olusturulma_tarihi']

    def perform_create(self, serializer):
        serializer.save(yazar=self.request.user.username)

class BlogDetayView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogYazisi.objects.all()
    serializer_class = BlogYazisiSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsYazarOrReadOnly]
