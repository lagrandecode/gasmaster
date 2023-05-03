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



# This is order model 
# class Order(models.Model):
#     STATUS = (
#         ('Pending','Pending'),
#         ('Order Confirmed','Order Confirmed'),
#         ('Out of Delivery','Out of Delivery'),
#         ('Delivered','Delivered'),
#     )
#     delivery_status = models.CharField(max_length=50,null=True,choices=STATUS)
#     customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
#     product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
#     email = models.CharField(max_length=50,null=True)
#     address = models.CharField(max_length=500,null=True)
#     mobile = models.CharField(max_length=20,null=True)
#     order_date= models.DateField(auto_now_add=True,null=True)




# class Feedback(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
#     name=models.CharField(max_length=40)
#     feedback=models.CharField(max_length=500)
#     date= models.DateField(auto_now_add=True,null=True)

#     class Meta:
#         verbose_name_plural = 'Feedback'





