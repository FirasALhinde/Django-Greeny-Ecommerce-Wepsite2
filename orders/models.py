from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
import random
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

# توليد قيمة من 8 قيم
def generaste_code(length=8):
    number = '0123456789'
    return ''.join(random.choice(number) for _ in range(length))
    
    
# class CartOrder(models.Model):
#     user = models.ForeignKey(User,related_name='order_user',verbose_name=_('User'),on_delete=models.SET_NULL,null=True,blank=True)
#     code = models.CharField(_('Code'),max_length=8,default=generaste_code)
#     order_status = models.CharField(_('Order Status'),max_length=10,choices=STATUS_CHOICES)
#     order_time = models.DateTimeField(_('Order Time'),default=timezone.now)
#     delivery_time = models.DateTimeField(_('Delivery Time'),null=True,blank=True)
#     def __str__(self):
#         return self.code
# class CartOrderDetail(models.Model):
#     order = models.ForeignKey(CartOrder,related_name='order_detail',on_delete=models.CASCADE,verbose_name=_('Order'))
#     product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_("Product"),related_name='order_product')
#     quantity = models.FloatField(_("Quantity"))
#     price = models.FloatField(_("Price"))
#     def __str__(self):
#         return str(self.order)


STATUS_CHOICES = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),

)

class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_user',verbose_name=_('User'),on_delete=models.SET_NULL,null=True,blank=True)
    code = models.CharField(_('Code'),max_length=8,default=generaste_code)
    order_status = models.CharField(_('Order Status'),max_length=10,choices=STATUS_CHOICES)
    order_time = models.DateTimeField(_('Order Time'),default=timezone.now)
    delivery_time = models.DateTimeField(_('Delivery Time'),null=True,blank=True)
    def __str__(self):
        return self.code
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE,verbose_name=_('Order'))
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_("Product"),related_name='order_product')
    quantity = models.FloatField(_("Quantity"))
    price = models.FloatField(_("Price"))
    def __str__(self):
        return str(self.order)