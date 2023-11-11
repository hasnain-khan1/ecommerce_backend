from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework import routers

from user_management.views import UserView

# from .views import get_user

# router.register("seller", SellerView, basename="seller_router")

app_name = "user_management_urls"

router = routers.DefaultRouter()
router.register("user", UserView, basename="user_router")

urlpatterns = [
    path("auth/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", include(router.urls))
    # path('user/<int:user_id>/', get_user, name='get_user')
]
