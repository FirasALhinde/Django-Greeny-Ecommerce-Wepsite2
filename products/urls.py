from django.urls import path
from .import views

app_name = 'products'

urlpatterns = [
    path('',views.ProductList.as_view(),name='product_list'),
    path('<slug:slug>',views.ProductDetail.as_view(),name='product_detail'),
    path('category/',views.CategoryList.as_view(),name='category_list'),
    path('brand/',views.BrandList.as_view(),name='brand_list'),
    path("brand/<slug:slug>",views.BrandDatail.as_view(),name = 'brand_detail')
]
