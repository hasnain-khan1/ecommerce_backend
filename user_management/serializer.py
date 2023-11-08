from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers

from user_management.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=60, write_only=True)

    class Meta:
        model = UserModel
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
            "confirm_password",
            "is_admin"
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
            "is_admin": {"read_only": True},
        }

    def save(self):
        del self.validated_data["confirm_password"]

        user = UserModel(**self.validated_data)
        user.set_password(self.validated_data.get("password"))
        user.save()
        return user

    def validate(self, data):
        data = super().validate(data)
        try:
            if not data.get("password") == data.get("confirm_password"):
                raise serializers.ValidationError({"error": "Password doesn't match"})
            validate_password(password=data.get("password"))
            return data
        except exceptions.ValidationError as e:
            errors = {"password": list(e.messages)}
            raise serializers.ValidationError(errors)
