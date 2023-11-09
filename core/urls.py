from django.urls import path, include
from rest_framework import routers
from .views import CategoryView, ProductView, CartItemView, CheckoutView, CartView


router = routers.DefaultRouter()
router.register('category', CategoryView, basename="category_urls")
router.register('product', ProductView, basename="product_urls")
router.register('cart', CartView, basename="cart_urls")
router.register('checkout', CheckoutView, basename="checkout_urls")
router.register('cart_item', CartView, basename="cart_item_urls")

urlpatterns = [

    path("", include(router.urls)),
    path("seller_product", ProductView.as_view({'get': 'seller_products'}), name="seller products")
    # path('main_categories/', CategoryList.as_view(), name='category-list'),
]
