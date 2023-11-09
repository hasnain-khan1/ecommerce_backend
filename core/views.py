from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Category, Product, Cart, CartItem, Checkout
from .serializers import CategorySerializer, ProductSerializer, CheckoutSerializer, CartSerializer, CartItemSerializer


# class CategoryList(APIView):
#     def get(self, request, format=None):
#         categories = Category.objects.filter(parent=None)
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

class CategoryView(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CheckoutView(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class CartItemView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
