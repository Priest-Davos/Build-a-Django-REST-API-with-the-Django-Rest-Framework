from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics

class ProductDetailApiView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class=ProductSerializer
  # lookup_field = "title"or whatever you want as pk (primary key)


class ProductCreateAPIView(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # print(queryset)
  def perform_create(self, serializer):
      # Accessing and printing values before saving (will not include computed fields)
      sale_price = serializer.validated_data.get("sale_price", None) #validated data
      discount_percentage = self.request.data.get('discount_percentage', 70) #invalidated data
      print("Before save:")
      print("sale price:", sale_price)  #None
      print("Discount Percentage:", discount_percentage) #10
      
      # Save the instance
      instance = serializer.save( )
      # Override get_discount method
      print(instance.get_discount()) # 80  # since in model it returns static value
      instance.get_discount = lambda: int(discount_percentage)
      # instance.save()
 
      # Accessing and printing values after saving (will include computed fields)
      print("\nAfter save:")
      print("Sale Price:", instance.sale_price)
      print("Discount Percentage:", instance.get_discount())