from django.shortcuts import render
from . import models
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import ProductSerializers,GasNewsSerializer

from .models import *


# Create your views here.


#this is the product feed
@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        api = Product.objects.all()
        serializers = ProductSerializers(api,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = ProductSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET','PUT','DELETE'])
def product_view(request,pk):
    try:
        api = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializers = ProductSerializers(api)
        return Response(serializers.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = ProductSerializers(api,data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        api.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def news_list(request):
    if request.method == 'GET':
        news = GasNews.objects.all()
        serializers = GasNewsSerializer(news,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = GasNewsSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



#this is the news feed 
@api_view(['GET','PUT','DELETE'])
def news_view(request,pk):
    try:
        news = GasNews.objects.get(id=pk)
    except GasNews.DoesNotExist:
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializers = GasNewsSerializer(news)
        return Response(serializers.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = GasNewsSerializer(news,data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.data,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
