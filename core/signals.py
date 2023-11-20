from django.db.models.signals import post_save
from django.dispatch import receiver
from.models import BuyProduct


@receiver(post_save, sender=BuyProduct)
def update_out_of_stock_status(sender, instance, **kwargs):
    cart_items = instance.checkout.cart.cartitem_set.all()
    for each in cart_items:
        quantity = each.quantity
        product_variation = each.variation
        var_quantity = product_variation.quantity
        var_quantity -= quantity
        if var_quantity == 0:
            product_variation.out_of_stock = True
        product_variation.quantity = var_quantity
        product_variation.save()

