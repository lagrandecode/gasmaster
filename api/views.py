from django.shortcuts import render
from . import models
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import *


# Create your views here.

@api_view(['GET','POST'])
def api_list(request):
    if request.method == 'GET':
        api = Product.objects.all()
        serializers = ProductSerializers(api,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializers = ProductSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



