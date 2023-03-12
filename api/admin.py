from django.contrib import admin
from .models import Product,GasNews,Order,Customer,Feedback

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','photo','discount','selling_price')
admin.site.register(Product,ProductAdmin)



class GasNewsAdmin(admin.ModelAdmin):
    list_display = ('news_link',)
admin.site.register(GasNews,GasNewsAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','address','mobile')
admin.site.register(Customer,CustomerAdmin)


admin.site.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('email','address','mobile','delivery_status')

admin.site.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name','feedback','date')
