from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from.models import Product,Brand,Category,Review,ProductImages


class ProductImagesInline(admin.TabularInline):#  ب تنعرض تحت
    model = ProductImages

class ProductAdmin(SummernoteModelAdmin):
    inlines = [ProductImagesInline]
    summernote_fields = '__all__'

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImages)
admin.site.register(Category)
