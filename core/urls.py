from django.urls import path, include
from rest_framework import routers
from .views import CategoryView, ProductView, CartItemView, CheckoutView, CartView, BuyProductView, ReviewView, \
    ProductVariationView, ProductAttributeView

router = routers.DefaultRouter()
router.register('category', CategoryView, basename="category_urls")
router.register('product', ProductView, basename="product_urls")
router.register('cart', CartView, basename="cart_urls")
router.register('checkout', CheckoutView, basename="checkout_urls")
router.register('cart_item', CartItemView, basename="cart_item_urls")
router.register('buy_product', BuyProductView, basename='buy_products')
router.register('review', ReviewView, basename='reviews')
router.register('product_variation', ProductVariationView, basename='variation')
router.register('product_attributes', ProductAttributeView, basename='attributes')


urlpatterns = [

    path("", include(router.urls)),
    path("seller_product", ProductView.as_view({'get': 'seller_products'}), name="seller products"),
    path('search_product', ProductView.as_view({'get': 'search_product'}), name="searching"),
    # path('main_categories/', CategoryList.as_view(), name='category-list'),
]
