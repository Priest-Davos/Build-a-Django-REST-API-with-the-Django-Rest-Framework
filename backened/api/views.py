# from django.http import JsonResponse
import json

from products.models import Product
from django .forms.models import model_to_dict

from  rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])  #add it   ... can specify more methods like POST ,  etc
def api_home(request, *args, **kwargs):
  model_data=Product.objects.all()
  data={}
  # data=[]
  if model_data:
    for product in model_data:
        # print(product.sale_price)
        product_data=model_to_dict(product)
        # product_data=model_to_dict(product, fields=['price']) # can also specify filds which we want to include 
        # data.append(product_data)
        data[product.id]=product_data

    # data=json.dumps(data)
  # return JsonResponse(data,safe=False)  # remove it
  return Response(data)   #add rest_Framework Response