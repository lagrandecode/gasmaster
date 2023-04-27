from django.contrib import admin
from .models import Product,Customer,Feedback

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','photo','discount','selling_price')
admin.site.register(Product,ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','address','mobile')
admin.site.register(Customer,CustomerAdmin)






class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name','feedback','date')
admin.site.register(Feedback,FeedbackAdmin)
