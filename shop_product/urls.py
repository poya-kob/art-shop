from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet,CategoryViewSet

router = DefaultRouter()
router.register(r'product', ProductsViewSet, basename="product")
router.register(r'category', CategoryViewSet, basename="category")

urlpatterns = [
    path('', include(router.urls)),

]
