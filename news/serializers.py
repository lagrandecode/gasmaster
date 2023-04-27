from rest_framework import serializers
from .models import GasNews


class GasNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasNews
        fields = '__all__'