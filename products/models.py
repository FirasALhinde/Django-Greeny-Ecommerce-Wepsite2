from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils import timezone
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

# Create your models here.
FLAT_TYPE = (
    ('New','New'),
    ('Feature','Feature')
)
class Product(models.Model):
    name = models.CharField(_("Name"),max_length=100)
    sku = models.IntegerField(_('SKU'))
    brand = models.ForeignKey('Brand',related_name='product_brand',verbose_name=_('Brand'),on_delete=models.SET_NULL,null=True,blank=True)
    price = models.FloatField(_('Price')) 
    desc = models.TextField(_('Desc'),max_length=10000)
    tags = TaggableManager(blank=True)
    flat = models.CharField(_("Flat"),max_length=10,choices=FLAT_TYPE) 
    category = models.ForeignKey('Category',related_name='product_category',verbose_name=_('Category'),on_delete=models.SET_NULL,null=True,blank=True)
    slug = models.SlugField(_('Slug'),null=True,blank=True)

    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Product, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.name
class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='product_image',verbose_name=_('Product'),on_delete=models.CASCADE)
    image = models.ImageField(_('Image'),upload_to='Product/')
    def __str__(self):
        return str(self.product)

class Brand(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    image = models.ImageField(_('Image'),upload_to='Brand/')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    image = models.ImageField(_('Image'),upload_to='Category/')
    def __str__(self):
        return self.name

class Review(models.Model):
    product =  models.ForeignKey(Product,related_name='review_product',verbose_name=_('Product'),on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='review_auther',verbose_name=_('User'),on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(_('Review'),max_length=500)
    rate = models.IntegerField(_('Rate'),default=0,validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    created_at = models.DateTimeField(_('Created_at'),default=timezone.now) 
    def __str__(self):
        return f'{self.user.username} - {self.product.name}'