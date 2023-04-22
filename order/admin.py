from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('email','address','mobile','delivery_status')
admin.site.register(Order,OrderAdmin)
