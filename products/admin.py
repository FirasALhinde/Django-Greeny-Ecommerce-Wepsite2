from django.contrib import admin
from.models import Product,Brand,Category,Review,ProductImages


class ProductImagesInline(admin.TabularInline):#  ب تنعرض تحت
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImages)
admin.site.register(Category)
