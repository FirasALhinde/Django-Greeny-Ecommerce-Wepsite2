#admin,py
class PostAdmin(admin.ModelAdmin):
list_display = ('id','title','publish_date')
search_fields = ['title','content']
date_hierarchy = 'publish_date'

**********************\_\_\_\_**********************-
'''

# setting media & static

static \_ media :

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

---

https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html

---

'''

# class based view

https://ccbv.co.uk/
https://simpleisbetterthancomplex.com
'''

'''

# slug

from django.template.defaultfilters import slugify
def save(self, *args, \*\*kwargs):
self.slug = slugify(self.name)
super(Product, self).save(*args, \*\*kwargs)
path('<slug:slug>',views.ProductDetail.as_view(),name='product_detail'),
'''

# Django Packages

https://djangopackages.org/
-- taggit
from taggit.managers import TaggableManager
tags = TaggableManager(blank=True)
'''
'''

# حساب كم منتج ب صنف

class CategoryList(ListView):
model = Category
paginate_by = 1
def get_context_data(self, **kwargs):
context = super().get_context_data(**kwargs)
context["categories"] = Category.objects.all().annotate(product_count = Count('product_category'))
return context

'''

'''

# Editor in field (text field)

https://summernote.org/
https://github.com/summernote/django-summernote

'''

'''
User : [model , auth-view , groups , permissions ] - AbstactBaseUser : [all program me : from skratch ):] - AbstactUser : [auth-view , groups , permissions] - one to one : User : Profile
'''

'''
add app setting to wepsite
'''

'''
signal : 2 event related example (1 -user singup ->2- create profile)
sender ------> reciever : action
5 types : - pre : 1: قبل ما يفتح نفذ init 2: save قبل ما يحفظ نفذ - post :1: بعد ما يفتح نفذ init 2: save قبل ما يحفظ نفذ - m2m_changed اذا العلاقة كثير ل كثير واتعدل شي من وحدة عدل ثانية
from django.db.models.signals import post_save
from django.dispatch import receiver

'''

'''

# send email

https://stackoverflow.com/questions/66841759/im-trying-to-send-an-email-from-django-using-gmail-smtp

'''

'''

# debug[qurey] (toolbar:libarary)

https://pypi.org/project/django-debug-toolbar/
https://django-debug-toolbar.readthedocs.io/en/latest/

'''

'''
# create data 

python faker
https://faker.readthedocs.io/en/master/
'''
'''

https://www.django-rest-framework.org/

'''

