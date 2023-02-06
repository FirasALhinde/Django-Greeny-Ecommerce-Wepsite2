# view.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

from .models import Product
from rest_framework import generics



@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()
    data = ProductSerializer(products,many=True).data
    return Response({'Success':True,'Product List':data})



class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer