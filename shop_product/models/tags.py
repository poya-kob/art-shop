from django.db import models

from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels

class Tags(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    created_time = jmodels.jDateTimeField(auto_now_add=True, verbose_name=_('created time'))
    active = models.BooleanField(default=True, verbose_name=_('inactive/active'))
    products = models.ManyToManyField('Products', related_name='tags', blank=True, verbose_name=_('products'))

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.title