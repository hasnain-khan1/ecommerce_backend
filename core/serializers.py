from rest_framework import serializers

from .models import Category, Product, Cart, CartItem, Checkout, BuyProduct


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = '__all__'


class BuyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyProduct
        fields = '__all__'
