from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# from rest_framework import APIView
from rest_framework import status
from .models import Order
from . import serializers
# Create your views here.


class OrderListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()
    def get(self,request):
        order = Order.objects.all()
        serializers = self.serializer_class(order,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
        

    def post(self,request):
        print(request)
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
