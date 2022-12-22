from uuid import uuid4

from rest_framework.serializers import ModelSerializer

from apps.models import Category, Shop, Product, ProductImage


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')


class ShopModelSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'description', 'image')


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'product')

