from django.urls import path

from .views import CategoryList

urlpatterns = [
    path('main_categories/', CategoryList.as_view(), name='category-list'),
]
