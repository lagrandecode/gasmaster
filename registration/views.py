from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import User,Addition



# Create your views here.

# //This method is used to send email to users 


def send_otp(email):
    subject = 'ACCOUNT VERIFICATION'
    otp = random.randint(1000,9999)
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email],fail_silently=False,)
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()




class UserCreationView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    def post(self,request):
        user_serializer
        


class AdditionView(generics.GenericAPIView):
    queryset = Addition.objects.all()
    serializer_class = AddionSerializer
    def post(self,request):
        addition_serializer= self.AddionSerializer(data=request.data)

        if addition_serializer.is_valid():

            addition_serializer.save()
            return Response({'meessage':'hllo'})



class UserandProfileView(generics.GenericAPIView):
    queryset = UserCreationSerializer.objects.all()
    serializer_class = UserCreationSerializer
    def post(self,request):
        user_serializer= self.UserCreationSerializer(data=request.data)
        if user_serializer.is_valid():
            
            addition_serializer.save()
            return Response({'meessage':'hllo2'})



    def post(self,request):
        user_serializer = self.UserCreationSerializer(data=request.data)
        addition_serializer= self.AddionSerializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True) and addition_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
            addition_serializer.save(user=user)
            return Response({"message": "Data saved successfully."})
        return Response({"message": "Data validation failed."})



# class UserCreateView(generics.GenericAPIView):
#     serializer_class = serializers.UserCreationSerializer
#     queryset = User.objects.all()

#     def post(self,request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             send_otp(serializer.data['email'])
#             return Response(data=({'message':'account created, check your email for OTP'},serializer.data),status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class VerifyView(generics.GenericAPIView):
    serializer_class = serializers.VerifySerializer
    try:
        def post(self,request):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.get(email=email)
                if not user.exist():
                    return Response({message:'something is wrong',
                    data:'Invalid Email'
                    },status=status.HTTP_400_BAD_REQUEST)
                if user[0].otp !=otp:
                    return Response({message:'something went wrong',data:'wring otp'},
                    status=status.HTTP_400_BAD_REQUEST)
                user = user.first()
                user.isVerified = True
                user.save()
                return Response({message:'Account verified',data:{}
                },status=status.HTTP_200_OK)
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)