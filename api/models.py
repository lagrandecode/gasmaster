from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductModel(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    discount = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    photo = models.ImageField()
    kg = models.PositiveIntegerField()

    def __str__(self):
        return self.product_name


#This class will show the news in the carousel (blog)
class GasNews(models.Model):
    news_image = models.ImageField()
    news_desc = models.CharField(max_length=1000)
    news_link = models.URLField()
    created_date = models.DateField(auto_now_add=True)

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pics = models.ImageField(upload_to='images/',null=True,blank=True)



