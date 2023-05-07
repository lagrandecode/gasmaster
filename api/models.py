from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    discount = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField(null=True,blank=True)
    photo = models.ImageField(upload_to='productimages/',blank=True,null=True)
    kg = models.PositiveIntegerField()

    def __str__(self):
        return self.product_name


# This is customer model 
class Customer(models.Model):
    name = models.CharField(max_length=250)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pics = models.ImageField(upload_to='images/',null=True,blank=True)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=200, null=False)


