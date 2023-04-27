from django.contrib import admin
from .models import GasNews

# Register your models here.
class GasNewsAdmin(admin.ModelAdmin):
    list_display = ('news_link',)
admin.site.register(GasNews,GasNewsAdmin)