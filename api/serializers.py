from rest_framework import serializers
from .models import *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        models = Product
        fields = '__all__'