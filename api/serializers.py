from rest_framework import serializers
from .models import Image, Tag

class _ImageModelSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='image-detail', lookup_field='pk')
    class Meta:
        model = Image

class _TagModelSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='tag-detail', lookup_field='pk')
    class Meta:
        model = Tag

class ImageModelSerializer(serializers.ModelSerializer):
    tags = _TagModelSerializer(many=True, read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='image-detail', lookup_field='pk')
    class Meta:
        model = Image

class TagModelSerializer(serializers.ModelSerializer):
    image_detail = _ImageModelSerializer(read_only=True, source='image')
    link = serializers.HyperlinkedIdentityField(view_name='tag-detail', lookup_field='pk')
    class Meta:
        model = Tag

