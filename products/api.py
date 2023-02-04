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


# genraic class
class ProuductListApi(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().filter(pk=2)


class ProuductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



# class based view

class ProductDetailApi(generics.GenericAPIView):
    queryset = Product
    serializer_class = ProductSerializer
    def get(self,request,*args, **kwargs):
        prouduct = self.get_object()
        data = ProductSerializer(prouduct).data
        return Response(data)

    def get_object(self,pk):
        return Product.objects.get(pk=pk)

    def patch(self,request,*args, **kwargs):
        prouduct = self.get_object()
        serializer = ProductSerializer(prouduct,data = request.data)
        serializer.is_valid(raise_exciption = True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,*args, **kwargs):
        prouduct = self.get_object()
        prouduct.delete()
        return Response({'Success':True})