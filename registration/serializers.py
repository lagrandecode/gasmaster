from rest_framework import serializers
from .models import User




class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=35)
    email = serializers.EmailField(max_length=80)
    phone_number = serializers.CharField(max_length=14)
    password = serializers.CharField(max_length=18,write_only=True)
    address = serializers.CharField(max_length=50)

    class Meta:
        model=User
        fields=['username','email','phone_number','password','address']

    def validate(self,attrs):
        username_exists=User.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(detail='User with username exist')

        email_exists=User.objects.filter(username=attrs['email']).exists()
        if email_exists: 
            raise serializers.ValidationError(detail='User with email exist')

        phone_number_exists=User.objects.filter(username=attrs['phone_number']).exists()
        if email_exists:
            raise serializers.ValidationError(detail='User with phone_number exist')
        address_exists=User.objects.filter(username=attrs['address']).exists()
        if address_exists:
            raise serializers.ValidationError(detail='User with address exist')

        return super().validate(attrs)

    # hashing the password 
    def create(self,validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user