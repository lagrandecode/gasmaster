from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework import generics
from . import serializers
from .models import Feedback
# Create your views here.


class FeedbackView(generics.GenericAPIView):
    def get(self,request):
        pass
    def post(self,request):
        pass 

    
