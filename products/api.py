# view (api)
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers  import ProductSerializer
from . models import Product

# function
@api_view(['Get'])
def product_list_api(request):
    products = Product.objects.all()
    data = ProductSerializer(products,many = True).data
    return Response({'Success':True,'ProuductList':data})


# genraic class
class ProuductListApi(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().filter(pk=2)


class ProuductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



# class based view

class ProductApi(generics.GenericApiView):
    queryset = Product
    serializer_class = ProductSerializer
    def get(self,request,*args, **kwargs):
        prouduct = self.get_object()
        data = ProductSerializer(prouduct).data
        return Response(data)

    def put(self,request,*args, **kwargs):
        pass

    def delete(self,request,*args, **kwargs):
        pass