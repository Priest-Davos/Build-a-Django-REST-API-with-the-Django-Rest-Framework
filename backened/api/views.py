# from django.http import JsonResponse
import json

from products.models import Product
from django .forms.models import model_to_dict

from  rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer

@api_view(['GET' ,'POST'])  #add it   ... can specify more methods like POST ,  etc
def api_home(request, *args, **kwargs):
  model_data=Product.objects.all()
  data=[]
  if (request.method=="GET"):
      if model_data:
        for product in model_data:

            # product_data=model_to_dict(product)  #or
            # product_data=model_to_dict(product, fields=['id','title','price']) # can also specify filds which we want to include 
            # data.append(product_data)
                                   #or use serializer
            serializer = ProductSerializer(product) #Create an instance of ProductSerializer for the current Product instance.
            data.append(serializer.data)#Serialize the Product instance using ProductSerializer and append the serialized data to the data list.

      return Response(data)   #add rest_Framework Response
  elif (request.method=="POST"):
      serializer=ProductSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):# Check if the serializer data is valid, raise an exception if not
          print(serializer.validated_data)
          instance = serializer.save()  # Save the data and get the instance
          print(instance)
          data.append (serializer.data)
      else:
        print("invalid serializer")
      
      return Response(data)