from django.db import models

class Customer(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=300)

    @staticmethod
    def check_email(email):
        # Customer.objects.filter(category__name=category)
        return Customer.objects.filter(email=email)
    def get_password(email):
        # Customer.objects.filter(category__name=category)
        return Customer.objects.get(email=email)