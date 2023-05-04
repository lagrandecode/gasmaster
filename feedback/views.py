from django.shortcuts import render
<<<<<<< HEAD
from rest_framework import status
from rest_framework.response import Response
from rest_framework 

=======
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework import generics
from . import serializers
from .models import Feedback
>>>>>>> 916fbbdbb0a9507d657e7ad84134b2c8f0442de3
# Create your views here.


class FeedbackView(generics.GenericAPIView):
    def get(self,request):
        pass
    def post(self,request):
        pass 

    
