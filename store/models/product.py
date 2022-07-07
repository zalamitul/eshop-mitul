from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    shopname = models.CharField(max_length=30,default="krishna")
    category = models.ForeignKey(Category,on_delete=models.CASCADE , default=1)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="products/")



    @staticmethod
    def get_products(category):
        if category == 'all':
            return Product.objects.all()
        else:
            return Product.objects.filter(category__name= category)

    @staticmethod
    def get_products_byid(ids):
        if ids == 'all':
            return Product.objects.all()
        else:
            data=[]
            for id in ids:
                id=int(id)
                data1=Product.objects.get(pk=id)
                data.append(data1)
            return data