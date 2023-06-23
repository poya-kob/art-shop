from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from shop_account.models import User
from django_jalali.db import models as jmodels
from shop_product.managers import ProductsManager
from utils.upload_image import upload_image_path

UserModel: User = get_user_model()


class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("name"))
    image = models.ImageField(upload_to=upload_image_path, verbose_name=_("main image"))
    inventory = models.IntegerField(default=10, verbose_name=_("inventory"))
    short_description = models.TextField(max_length=700, verbose_name=_("short description"))
    full_description = models.TextField(verbose_name=_("full description"))
    created_time = jmodels.jDateTimeField(verbose_name=_("created time"), auto_now_add=True)
    category = models.ForeignKey('Categories', verbose_name=_("category"),related_name='products', on_delete=models.CASCADE)
    supplier = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_products',
                                 verbose_name=_("supplier"))
    active = models.BooleanField(default=False, verbose_name=_("active/inactive"))
    objects = ProductsManager()

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    @property
    def is_new(self):
        day_passed = (datetime.now().date() - self.created_time.date()).days
        return day_passed <= 5

    def __str__(self):
        return self.name
