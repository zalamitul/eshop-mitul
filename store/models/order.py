import datetime

from django.db import models
from .product import Product
from .customer import Customer

class Order(models.Model):
    product=models.ForeignKey(Product , on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer ,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    date=models.DateField(default=datetime.datetime.today)
    image = models.ImageField(upload_to="products/")
    phone=models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    status = models.CharField(max_length=50,default='pandding')
