from django.shortcuts import render
from . import serializers
from .models import GasNews
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated
# Create your views here.

class GasNewsList(generics.GenericAPIView):
    serializer_class = serializers.GasNewsSerializer
    permission_classes = [IsAuthenticated]
    queryset = GasNews.objects.all()
    def get(self,request):
        try:
            news = GasNews.objects.all()

            serializers = self.serializer_class(news,many=True)
            return Response(serializers.data,status=status.HTTP_200_OK)
        except GasNews.DoesNotExist:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

            




