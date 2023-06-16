from django.db import models
from django.utils.translation import gettext_lazy as _

from django_jalali.db import models as jmodels
from django.contrib.auth import get_user_model

from shop_account.models import User

UserModel: User = get_user_model()


class ProductPrice(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE, related_name='price', verbose_name=_('product'))
    product_price = models.PositiveBigIntegerField(verbose_name=_("price"), default=0)
    off_price = models.PositiveBigIntegerField(verbose_name=_("off price"), null=True, blank=True, default=0)
    off_expired_time = jmodels.jDateTimeField(verbose_name=_("off expired time"), null=True, blank=True)
    supplier = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name=_("supplier"))

    class Meta:
        verbose_name = _("product price")
        verbose_name_plural = _("products prices")
