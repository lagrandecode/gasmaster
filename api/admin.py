from django.contrib import admin
from .models import Product,Customer

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','photo','discount','selling_price')
admin.site.register(Product,ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','address','mobile')
admin.site.register(Customer,CustomerAdmin)



<<<<<<< HEAD
=======



>>>>>>> 46b7e20d649232fb47c726ce4ac41dea607cdc37
