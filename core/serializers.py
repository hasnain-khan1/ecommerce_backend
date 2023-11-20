from rest_framework import serializers
from django.forms.models import model_to_dict
from .models import Category, Product, Cart, CartItem, Checkout, BuyProduct, Review, ProductVariation, ProductAttribute


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'slug', 'description', 'category', 'seller', 'created_at', 'deleted_at')

    @staticmethod
    def total_review(instance):
        reviews = instance.reviews.all()
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            return total_rating / len(reviews)
        else:
            return 0

    def to_representation(self, instance):
        if self.context['request'].method != "GET":
            return super().to_representation(instance)
        try:
            category = instance.category.all()
        except AttributeError:
            category = instance.first().category.all()
        serialized_category = CategorySerializer(category, many=True).data
        instance_dict = model_to_dict(instance)
        instance_dict['overall_review'] = self.total_review(instance)
        instance_dict['category'] = serialized_category
        instance_dict['image'] = instance.image.url if instance.image else ''
        return instance_dict


class ProductVariationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductVariation
        fields = '__all__'


class ProductAttributesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductAttribute
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user', 'products')

    def to_representation(self, instance):
        if self.context['request'].method == "GET":
            products = instance.products.all()
            serialized_product = ProductSerializer(products, many=True, context=self.context).data
            instance_dict = model_to_dict(instance)
            instance_dict['products'] = serialized_product
            return instance_dict

        return super().to_representation(instance)


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def to_representation(self, instance):
        if self.context['request'].method == "GET":
            products = instance.product
            serialized_product = ProductSerializer(products, context=self.context).data
            instance_dict = model_to_dict(instance)
            instance_dict['products'] = serialized_product
            return instance_dict

        return super().to_representation(instance)


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ('cart', 'shipping_address', 'payment_method', 'created_at', 'updated_at')

    def to_representation(self, instance):
        if self.context['request'].method != "GET":
            return super().to_representation(instance)
        products = instance.cart.cartitem_set.all()
        serialized_product = CartItemSerializer(products, many=True, context=self.context).data
        serialized_product = [{**i["product"], "quantity": i["quantity"]} for i in serialized_product]
        instance_dict = model_to_dict(instance)
        instance_dict['created_at'] = instance.created_at
        instance_dict['updated_at'] = instance.updated_at
        instance_dict['products'] = serialized_product
        return instance_dict


class BuyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyProduct
        fields = '__all__'

    def to_representation(self, instance):
        if self.context['request'].method == "GET":
            products = instance.checkout.cart.products.all()
            serialized_product = ProductSerializer(products, many=True, context=self.context).data
            instance_dict = model_to_dict(instance)
            instance_dict['created_at'] = instance.created_at
            instance_dict['updated_at'] = instance.updated_at
            instance_dict['products'] = serialized_product
            return instance_dict

        return super().to_representation(instance)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
