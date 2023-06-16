from django.db import models
from django.db.models import Q


class ProductsManager(models.Manager):

    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(category__name__iexact=category_name, active=True)

    def get_last_price(self, **kwargs):
        return self.get_queryset().filter(**kwargs).first().price.last()

    def get_user_products_with_price(self):
        # todo: complete this method
        pass

    def search(self, query):
        lookup = (
                Q(name__icontains=query) |
                Q(short_description__icontains=query) |
                Q(full_description__icontains=query) |
                Q(tags__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()
