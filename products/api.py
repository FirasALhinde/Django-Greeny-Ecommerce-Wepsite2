# view (api)
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers  import ProductSerializer
from . models import Product


@api_view(['Get'])
def product_list_api(request):
    products = Product.objects.all()
    data = ProductSerializer(products,many = True).data
    return Response({'Success':True,'ProuductList':data})



class ProuductListApi(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().filter(pk=2)


class ProuductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()