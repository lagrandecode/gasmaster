from django.db import models

# Create your models here.



# This is order model 
class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out of Delivery','Out of Delivery'),
        ('Delivered','Delivered'),
    )
    delivery_status = models.CharField(max_length=50,null=True,choices=STATUS)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
