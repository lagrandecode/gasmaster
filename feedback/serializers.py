from rest_framework import serializers
from .models import Feedback



class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'