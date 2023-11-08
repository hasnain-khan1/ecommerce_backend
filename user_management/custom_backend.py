# custom_auth_backends.py

from django.contrib.auth.backends import ModelBackend
from user_management.models import SellerModel, UserModel


class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Check if a Seller exists with the given username
        seller = SellerModel.objects.filter(username=username).first()
        if seller and seller.check_password(password):
            return seller

        # Check if a Buyer exists with the given username
        buyer = UserModel.objects.filter(username=username).first()
        return buyer if UserModel and buyer.check_password(password) else None
