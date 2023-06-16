from rest_framework.viewsets import ModelViewSet

from .models import Products


class ProductsView(ModelViewSet):
    queryset = Products.objects.get_active_products()
