from django.db import models

from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels


class Categories(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("name"), unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('parent'))
    created_time = jmodels.jDateTimeField(verbose_name=_("created time"), auto_now_add=True)
    active = models.BooleanField(default=False, verbose_name=_("active/inactive"))


    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name
    #
    # def save(self, *args, **kwargs):
    #     if self.parent is not None and self.parent.parent is not None:
    #         return _('you can not set this category as parent!')
    #     else:
    #         return super().save(*args, **kwargs)
