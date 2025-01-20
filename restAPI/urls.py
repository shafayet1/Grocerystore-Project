from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryViewSet, SupplierViewSet, ProductViewSet,
    CustomerViewSet, OrderViewSet, OrderDetailViewSet
)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order_details', OrderDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]