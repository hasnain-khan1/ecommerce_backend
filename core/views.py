from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Category, Product, Cart, CartItem, Checkout
from .serializers import CategorySerializer, ProductSerializer, CheckoutSerializer, CartSerializer, CartItemSerializer


class CategoryView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def seller_products(self, request):
        try:
            seller = self.request.user.id
            seller_product = self.get_queryset().filter(seller_id=seller)
            serialized_data = self.get_serializer(seller_product, many=True)
            return Response({'data': serialized_data.data, "message": "Successful"})
        except Exception as er:
            return Response({'data': [], "message": f"Error -> {er}"})


class CartView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CheckoutView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class CartItemView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
