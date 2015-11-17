from rest_framework import serializers
from .models import Image, Tag

class _ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image

class _TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag

class ImageModelSerializer(serializers.ModelSerializer):
    tags = _TagModelSerializer(many=True, read_only=True)
    class Meta:
        model = Image

class TagModelSerializer(serializers.ModelSerializer):
    image_detail = _ImageModelSerializer(read_only=True, source='image')
    class Meta:
        model = Tag

