from django.db import models

# Create your models here.

class ProductModel(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    discount = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    photo = models.ImageField()
    kg = models.PositiveIntegerField()


#This class will show the news in the carousel 
class GasNews(models.Model):
    news_image = models.ImageField()
    news_desc = models.CharField(max_length=1000)
    news_link = models.URLField()
