from django.db import models

# Create your models here.
class Product (models.Model):
  title=models.CharField(max_length=255)
  content=models.TextField(blank=True, null=True)
  price=models.DecimalField(max_digits=15,decimal_places=2,default=0)
  
  @property
  def sale_price(self):
    og_price=float(self.price)
    discount=80
    salePrice= "%.2f" %(og_price-float(og_price*discount/100))
    return salePrice
