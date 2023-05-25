from rest_framework import serializers
from .models import User
from .models import Addition




class UserCreationSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(max_length=80)
    # phone_number = serializers.CharField(max_length=14)
    # password = serializers.CharField(max_length=18,write_only=True)
    # address = serializers.CharField(max_length=50)
    # isVerified = serializers.BooleanField(default=False)

    class Meta:
        model=User
        fields=['email','phone_number','password','address','isVerified']


class VerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()


class AddionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addition
        fields = '__all__'