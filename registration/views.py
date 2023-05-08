from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers


# Create your views here.


class UserCreateView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=({'message':'account created, check your email for OTP'},serializer.data),status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)