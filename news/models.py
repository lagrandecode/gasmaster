from django.db import models

# Create your models here.


#This class will show the news in the carousel (blog)
class GasNews(models.Model):
    news_image = models.ImageField()
    news_desc = models.CharField(max_length=1000)
    news_link = models.URLField()
    created_date = models.DateField(auto_now_add=True)
