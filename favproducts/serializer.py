from rest_framework import serializers
from favproducts.models import Client, Product, FavoriteProduct
from favproducts.validators import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
    def validate(self,data):
        if not name_valid(data['name']):
            raise serializers.ValidationError({'name':"Não inclua números ou caracteres especiais neste campo"})
        return data

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class FavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProduct
        fields = '__all__'

class FavProductListSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.name')
    product = serializers.ReadOnlyField(source='product.title')
    price = serializers.ReadOnlyField(source='product.price')
    class Meta:
        model = FavoriteProduct
        fields = '__all__'