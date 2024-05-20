from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics

class ProductDetailApiView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class=ProductSerializer
  # lookup_field = "title"or whatever you want as pk (primary key)

