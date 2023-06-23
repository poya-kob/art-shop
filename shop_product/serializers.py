from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import Products, Categories


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = (
            'id', 'name', 'image', 'inventory', 'short_description', 'created_time', 'category', 'supplier', 'active',
            'is_new')


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
    # def create(self, validated_data):
    #     cat_name = validated_data.pop


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name', 'parent', 'active')

    def create(self, validated_data):
        parent = validated_data.get('parent')
        if parent is None:
            return Categories.objects.create(**validated_data)
        elif parent.parent is not None:
            raise Exception(_('you can not set this category as parent!'))
        return Categories.objects.create(**validated_data)
