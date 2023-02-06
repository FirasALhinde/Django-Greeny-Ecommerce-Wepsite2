from django.urls import path
from .import views
from .api import product_list_api ,ProuductListApi , ProuductDetailAPI , ProductDetailAPi
app_name = 'products'

urlpatterns = [
    path('',views.ProductList.as_view(),name='product_list'),
    path('test',views.product_list,name='p_l'),
    path('<slug:slug>',views.ProductDetail.as_view(),name='product_detail'),
    path('category/',views.CategoryList.as_view(),name='category_list'),
    path('category/<slug:slug>',views.CategoryDetail.as_view(),name='category_detail'),
    path('brand/',views.BrandList.as_view(),name='brand_list'),
    path("brand/<slug:slug>",views.BrandDatail.as_view(),name = 'brand_detail'),



    #api url
    path('api/list',product_list_api),
    path('api/list/cbv',ProuductListApi.as_view()),
    path('api/list/cbv/<int:pk>',ProuductDetailAPI.as_view()),
    path('api/cbv/<int:pk>',ProductDetailAPi.as_view())
]
