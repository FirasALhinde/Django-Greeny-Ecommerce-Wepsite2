from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Country (models.Model):
    name = models.CharField(_('Name'),max_length=50)

    class Meta:
        verbose_name_plural = 'Contries'
    def __str__(self):
        return self.name
class City(models.Model):
    country = models.ForeignKey(Country,related_name='city_country',verbose_name=_('Country'),on_delete=models.CASCADE)
    name = models.CharField(_('Name'),max_length=50)
    class Meta:
        verbose_name_plural = 'Citiess'
    def __str__(self):
        return self.name



class Company(models.Model):
    name = models.CharField(_('Name'),max_length=50)
    logo = models.ImageField(_('Logo'),upload_to='company/')
    about = models.CharField(_('About'),max_length=300)
    fb_link = models.URLField(_('Fb_Link'),null=True,blank=True)
    tw_link = models.URLField(_('Tw_link'),null=True,blank=True)
    ins_link = models.URLField(_('Ins_link'),null=True,blank=True)
    email = models.EmailField(_("Email"),max_length=30)
    phone_number = models.CharField(_('Phone Number'),max_length=20)
    address = models.CharField(_("Address"),max_length=100)

    def __str__(self):
        return self.name