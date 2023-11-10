from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.utils import timezone


class UserChoices(models.TextChoices):
    BUYER = 1, "Buyer"
    SELLER = 2, "Seller"


class StatusChoices(models.TextChoices):
    ACTIVE = 0, "Active"
    DELETED = 1, "Deleted"


class UserModel(AbstractUser):
    user_type = models.CharField(max_length=10, choices=UserChoices.choices, null=True, blank=True)
    status = models.CharField(max_length=12, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        """
        Override the delete method to update the 'status' field instead of hard delete.
        """
        self.status = StatusChoices.DELETED  # Update the 'status' field to your desired value
        self.deleted_at = timezone.now()
        self.save()


# class SellerModel(AbstractUser):
#
#     company_name = models.CharField(max_length=255, null=True, blank=True)
#     user_permissions = models.ManyToManyField(Permission, blank=True, related_name='seller_permissions')
#     groups = models.ManyToManyField(Group, blank=True, related_name="seller_groups")
