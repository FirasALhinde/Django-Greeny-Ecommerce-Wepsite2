from django.shortcuts import render
from products.models import Category , Product
from django.db.models import Count
# Create your views here.

def home(request):
    categories = Category.objects.all().annotate(product_count = Count('product_category'))
    featured_product = Product.objects.filter(flat = 'Feature')[:6]
    return render(request,'home/home.html',{
        'categories':categories,
        'featured_product':featured_product,
    })