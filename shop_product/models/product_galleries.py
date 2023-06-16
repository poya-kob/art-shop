from django.db import models

from django.utils.translation import gettext_lazy as _

from utils.upload_image import upload_image_path
class ProductsGalleries(models.Model):
    title = models.CharField(max_length=120, verbose_name=_("title"))
    image = models.ImageField(upload_to=upload_image_path, verbose_name=_("image"))
    product = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name=_("product"), related_name='gallery')
    active = models.BooleanField(default=False, verbose_name=_("active / inactive"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("products gallery")
        verbose_name_plural = _("products galleries")