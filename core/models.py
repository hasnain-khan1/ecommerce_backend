from django.db import models
from user_management.models import UserModel, StatusChoices
from django.utils import timezone


class LogsMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=12, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Category(LogsMixin):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name="children", on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def delete(self, using=None, keep_parents=False):
        """
        Override the delete method to update the 'status' field instead of hard delete.
        """
        self.status = StatusChoices.DELETED  # Update the 'status' field to your desired value
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Product(LogsMixin):
    name = models.CharField(max_length=300)
    seller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="seller_products")
    category = models.ManyToManyField(Category, blank=True, related_name="category_products")
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sales_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        """
        Override the delete method to update the 'status' field instead of hard delete.
        """
        self.status = StatusChoices.DELETED  # Update the 'status' field to your desired value
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Review(LogsMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()


class Checkout(LogsMixin):
    cart = models.ForeignKey("Cart", related_name="cart_checkout", on_delete=models.CASCADE)
    shipping_address = models.TextField()
    payment_method = models.CharField(max_length=100)

    def delete(self, using=None, keep_parents=False):
        """
        Override the delete method to update the 'status' field instead of hard delete.
        """
        self.status = StatusChoices.DELETED  # Update the 'status' field to your desired value
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.cart}-{self.cart}-checkout"


class Cart(LogsMixin):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True, through='CartItem')

    def delete(self, using=None, keep_parents=False):
        """
        Override the delete method to update the 'status' field instead of hard delete.
        """
        self.status = StatusChoices.DELETED  # Update the 'status' field to your desired value
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"Cart for {self.user}"


class CartItem(LogsMixin):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # You can track the quantity of each product in the cart

    def delete(self, using=None, keep_parents=False):
        """
        Override the delete method to update the 'status' field instead of hard delete.
        """
        self.status = StatusChoices.DELETED  # Update the 'status' field to your desired value
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart"


class BuyProduct(LogsMixin):
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, related_name="product_checkout")

    def delete(self, using=None, keep_parents=False):
        """
        Override the delete method to update the 'status' field instead of hard delete.
        """
        self.status = StatusChoices.DELETED  # Update the 'status' field to your desired value
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.checkout}"

