from django.db import models
from api.models import Customer

# Create your models here.

class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)

    class Meta:
        verbose_name_plural = 'Feedback'