from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
  discount_percentage=serializers.SerializerMethodField()
  class Meta:
        model = Product
        fields=[
          "title",
          "content",
          "price",
          "sale_price",
          "discount_percentage"
        ]
  def get_discount_percentage(self,obj):
       return obj.get_discount()