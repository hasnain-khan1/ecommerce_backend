# from django.contrib import admin
#
# from .models import Product, Category
#
# Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)
from django.apps import apps
from django.contrib import admin

app = apps.get_app_config('core')
models = app.get_models()

for model in models:
    admin.site.register(model)
