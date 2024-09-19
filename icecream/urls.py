from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IceCreamViewSet, CustomerViewSet

router = DefaultRouter()
router.register('icecreams', IceCreamViewSet)
router.register('customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]