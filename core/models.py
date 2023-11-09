# from django.contrib.auth import get_user_model
from django.db import models
from user_management.models import UserModel, SellerModel

# User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name="children", on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True)
    products = models.ManyToManyField("Product", related_name="category_products")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300)
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE, related_name="seller_products")
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Checkout(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    shipping_address = models.TextField()
    payment_method = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # You can track the quantity of each product in the cart

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart"
