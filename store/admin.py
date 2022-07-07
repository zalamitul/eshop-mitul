from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.order import Order

# Register your models here.
class adminorder(admin.ModelAdmin):
    list_display = ["product","customer","quantity","price","date","image"]

class adminproduct(admin.ModelAdmin):
    list_display = ["name","shopname", "price", 'category']


class admincategory(admin.ModelAdmin):
    list_display = ['name']



class admincustomer(admin.ModelAdmin):
    list_display = ['fname','lname','email','phone','password']

admin.site.register(Product, adminproduct)
admin.site.register(Category,admincategory)
admin.site.register(Customer,admincustomer)
admin.site.register(Order,adminorder)