from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('שם קטגוריה'))
    image = models.ImageField(upload_to='category_images/', verbose_name=_('תמונה'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("קטגוריה")
        verbose_name_plural = _("קטגוריות")

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('קטגוריה'))
    name = models.CharField(max_length=100, verbose_name=_('שם מוצר'))
    description = models.TextField(verbose_name=_('תיאור'))
    image = models.ImageField(upload_to='product_images/', verbose_name=_('תמונה'))

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = _("מוצר")
        verbose_name_plural = _("מוצרים")



class About(models.Model):
    # content = models.TextField(verbose_name=_('תוכן'))
    # content = RichTextUploadingField(verbose_name=_('תוכן'))
    # title=models.CharField('Title', max_length=200)
    content=CKEditor5Field('Text', config_name='extends',)

    def __str__(self):
        return "תוכן דף אודות"

    class Meta:
        verbose_name = _("עמוד אודות")
        verbose_name_plural = _("עמוד אודות")


class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/', verbose_name=_('תמונה'))
    caption = models.CharField(max_length=255, blank=True, verbose_name=_('כיתוב'))

    def __str__(self):
        return self.caption if self.caption else "תמונת קרוסלה"

    class Meta:
        verbose_name = _("תמונת קרוסלה")
        verbose_name_plural = _("תמונות קרוסלה")