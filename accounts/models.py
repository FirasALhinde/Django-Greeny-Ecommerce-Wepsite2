from django.db import models
from django.utils.translation import gettext as _
from settings.models import Country,City
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE,verbose_name=_('User'))
    image = models.ImageField(_('Image'),upload_to='Profile/',null=True,blank=True)
    def __str__(self):
        return self.user.username
# create user -----> create profile
@receiver(post_save,sender=User)
def create_profile(sender,instance,created ,**kwargs):# sender : من يلي بعت اشاؤة instatncd : هي داتا تبع مستخدم : createed : من ضمن البيانات يلي راحعة )(true: createed or false : edit) 
    if created: # singup only
        Profile.objects.create(user = instance)

DATA_TYPE = (
    ('Home','Home'),
    ('Office','Office'),
    ('Bussiness','Bussiness'),
    ('Academy','Academy'),
    ('Others','Others'),
)
class UserPhoneNumber(models.Model):
    user = models.ForeignKey(User,related_name='user_phone',on_delete=models.CASCADE,verbose_name=_('User'))
    phone_number = models.CharField(_('Phone Number'),max_length=15)
    type = models.CharField(max_length=10,choices=DATA_TYPE)
    def __str__(self):
        return self.user.username
class UserAddress(models.Model):
    user = models.ForeignKey(User,related_name='user_address',on_delete=models.CASCADE,verbose_name=_('User'))
    type = models.CharField(_("Type"),max_length=10,choices=DATA_TYPE)
    country = models.ForeignKey(Country,related_name='user_country',on_delete=models.SET_NULL,null=True,verbose_name=_('Country'))
    city = models.ForeignKey(City,related_name='user_city',on_delete=models.SET_NULL,null=True,verbose_name=_('City'))
    state = models.CharField(_('State'),max_length=50)
    ragion = models.CharField(_('Ragion'),max_length=50)
    street = models.CharField(_('Street'),max_length=50)
    notes = models.TextField(_('Notes'),max_length=300,null=True,blank=True)    
    def __str__(self):
        return f'{self.user.username} - {self.type}'