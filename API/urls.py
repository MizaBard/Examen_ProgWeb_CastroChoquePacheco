from django.urls import path, include
from rest_framework import routers
from API import views

router=routers.DefaultRouter()
router.register(r'producto', views.ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
