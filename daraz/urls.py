from django.contrib import admin
from django.urls import path, include
# from core.urls import core_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include("core.urls")),
]
