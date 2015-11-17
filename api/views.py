from django.shortcuts import render

from rest_framework import generics
from rest_framework import filters

from .models import Image, Tag
from .serializers import ImageModelSerializer, TagModelSerializer

class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageModelSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, )
    filter_fields = ('url', 'tags__uuid', 'tags__text', )
    search_fields = ('tags__text', )
    ordering_fields = ('updated', 'tags__text', 'url', 'uuid')

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageModelSerializer

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, )
    filter_fields = ('text', 'image', 'image__url', )
    search_fields = ('text', )
    ordering_fields = ('updated', 'text', 'image__url', 'uuid')

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer

