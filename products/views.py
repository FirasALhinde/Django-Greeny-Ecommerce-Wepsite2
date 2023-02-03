from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product,ProductImages,Review,Category,Brand
from django.db.models import Count
from django.db.models import Q , F
from django.contrib.auth.decorators import login_required

# Create your views here.

def product_list(request):
    # queryset = Product.objects.filter(name__endswith='fox',price__gt=40)
    # queryset = Product.objects.filter(
    #     Q(name__endswith='fox') &
    #     Q(price__gt=40))
    # queryset = Product.objects.all()
    # queryset.filter(name__endswith='fox').filter(price__gt=50)
    # return render(request,'products/list.html',{'data':queryset})
    # queryset = Product.objects.filter(id=F('category__id')) #لمقارنة عمودين مع به
    # queryset = Product.objects.order_by("name").reverse()
    # queryset = Product.objects.values_list('id','name','category__name').distinct()
    # queryset = Product.objects.only('id','name','category__name','price').distinct()
    # queryset = Product.objects.defer('id','category__name').distinct()
    # queryset = Product.objects.select_related('category').select_related("brand").all()  # prefetch_related ( many - to - many )
    queryset = Product.objects.select_related('category').select_related("brand").all() 


    return render(request,'products/list.html',{"data":queryset})
class ProductList(ListView):
    model = Product
    paginate_by = 50

class ProductDetail (DetailView):
    model = Product
    def get_context_data(self, **kwargs):
        myproduct = self.get_object()
        context = super().get_context_data(**kwargs)
        context["images"] = ProductImages.objects.filter(product = myproduct)
        context['reviews'] = Review.objects.filter(product = myproduct)
        return context


class CategoryList(ListView):
    model = Category
    paginate_by = 1
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(product_count = Count('product_category'))
        return context

class CategoryDetail(DetailView):
    pass

class BrandList(ListView):
    model = Brand
    paginate_by = 1    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all().annotate(brand_count = Count('product_brand')) 
        return context


class BrandDatail(DetailView):
    model = Brand
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brand_products"] = Product.objects.filter (brand=brand) 
        return context


@login_required
def add_review(request):
    pass

@login_required
def add_to_favourites(request):
    pass