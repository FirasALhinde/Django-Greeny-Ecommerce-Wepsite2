# view (api)
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers  import ProductSerializer
from . models import Product
from rest_framework.views import APIView


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


class ProuductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# class based view 
class ProductDetailAPi(generics.GenericAPIView):
    queryset = Product
    serializer_class = ProductSerializer
    def get(self,request,*args, **kwargs):
        product = self.get_object()
        data = ProductSerializer(product).data
        return Response(data)

    def patch(self,request,*args, **kwargs):
        product = self.get_object()
        serializer = ProductSerializer(product,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def delete(self,request,*args, **kwargs):
        product = self.get_object()
        product.delete()
        return Response({"Success":True})