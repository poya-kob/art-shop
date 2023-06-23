from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Products, Categories
from .serializers import ProductDetailSerializer, ProductListSerializer, CategoryCreateSerializer


class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.get_active_products()

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductDetailSerializer
        return ProductListSerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategoryCreateSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Categories.objects.all()
        return Categories.objects.filter(active=True)

    @action(detail=True, url_path='products', url_name='products-list')
    def category_products(self, request, *args, **kwargs):
        cat_serial = CategoryCreateSerializer(self.get_object())
        products_serial = ProductListSerializer(self.get_object().products.all(), many=True)
        data = {'category': cat_serial.data,
                'products': products_serial.data}
        return Response(data, status=status.HTTP_200_OK)
