from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
      
class ProductListAPIView(generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_create(self, serializer):
     
      discount_percentage = self.request.data.get('discount_percentage', 70) #invalidated data
      
      # Save the instance
      instance = serializer.save( )
      # Override get_discount method
      print(instance.get_discount()) # 80  # since in model it returns static value
      instance.get_discount = lambda: int(discount_percentage)
      instance.save()
      
@api_view(["GET","POST"])
def FuncBasedProduct_all_view(request,pk=None, *args,**kwargs):
    method=request.method
    queryset = Product.objects.all()
    serializer=ProductSerializer(queryset,many=True)
    if method=="GET":
      if pk!=None:
        # Retrieve a specific product by primary key
         try:
             product = Product.objects.get(pk=pk)
         except Product.DoesNotExist:
             return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
         serializer = ProductSerializer(product)
         return Response(serializer.data)

      
      # List all product
          
      data=serializer.data 
      return Response(data)
    
    elif method == "POST":
        # Create a new product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            discount_percentage = request.data.get('discount_percentage', 70)
            instance.get_discount = lambda: int(discount_percentage)
            instance.save()
            response_serializer = ProductSerializer(instance)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)