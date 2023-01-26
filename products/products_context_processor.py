from . models import Category,Brand


def get_brands(request):
    brands = Brand.objects.all()
    return {"c_brands":brands}