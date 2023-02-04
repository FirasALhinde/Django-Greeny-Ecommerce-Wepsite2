"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import url
# from rest_framework_swagger.views import get_swagger_view
from django.views.generic import TemplateView

# schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls',namespace='home')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('products/',include('products.urls',namespace='products')),
    path('orders/',include("orders.urls",namespace='orders')),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('__debug__/', include('debug_toolbar.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    # path('api-docs', schema_view),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('rest-auth/', include('dj_rest_auth.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)