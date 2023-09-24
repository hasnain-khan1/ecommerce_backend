from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class UserModel(AbstractBaseUser):
    email = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ["first_name"]
    objects = UserManager()

    def has_perm(self, perm, obj=None):  # noqa
        # For now, allow all permissions
        return True

    def has_module_perms(self, app_label):  # noqa
        # For now, allow all app modules
        return True

    def delete(self, using=None, keep_parents=False):
        # Check if the user is a superuser before allowing deletion
        if self.is_superuser:
            super(UserModel, self).delete(using=using, keep_parents=keep_parents)
        else:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied("Only superusers can delete entries.")
