#admin,py
class PostAdmin(admin.ModelAdmin):
    list_display  = ('id','title','publish_date')
    search_fields = ['title','content']
    date_hierarchy = 'publish_date'

________________________________________________-
'''
# setting media & static
static _ media :

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static/')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


urls.py
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''

'''
paginationm
_ _  _  _ _ 
https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html

----------
'''
# class based view
https://ccbv.co.uk/
https://simpleisbetterthancomplex.com
'''


'''
# slug
from django.template.defaultfilters import slugify
def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Product, self).save(*args, **kwargs)
 path('<slug:slug>',views.ProductDetail.as_view(),name='product_detail'),
'''
# Django Packages
https://djangopackages.org/
 -- taggit
 from taggit.managers import TaggableManager
tags = TaggableManager(blank=True)
'''