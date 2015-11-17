from rest_framework import serializers
from .models import Image, Tag

class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag

class ImageModelSerializer(serializers.ModelSerializer):
    tags = TagModelSerializer(many=True, read_only=True)
    class Meta:
        model = Image

