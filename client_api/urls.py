from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from client.views import ClientViewSet

router = routers.DefaultRouter()
router.register('clientes', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
