from rest_framework import serializers
from api.models import Category, Product, Order, Review
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'email', 'is_staff')

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    image = serializers.CharField(required=False)
    description = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
    category = CategorySerializer(read_only=True)

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product_name = serializers.CharField(required=True)
    count = serializers.IntegerField(required=True)
    class Meta:
        model = Order
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True)
    author = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
