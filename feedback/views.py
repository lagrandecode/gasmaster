from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework import generics
from . import serializers
from .models import Feedback
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.


class FeedbackView(generics.GenericAPIView):
    permission_class = [IsAuthenticated,]
    serializer_class = serializers.FeedbackSerializer
    quesryset = Feedback.objects.all()
    def get(self,request):
        feedback = Feedback.objects.all()
        serializers = self.serializer_class(feedback,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class FeedbackDetailView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = serializers.FeedbackSerializer
    def get(self,request,pk):
        feedback = get_object_or_404(Feedback,id=pk)
        serializers = self.serializer_class(feedback)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        feedback = get_object_or_404(Feedback,id=pk)
        serializers = self.serializer_class(feedback,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        feedback = get_object_or_404(Feedback,id=pk)
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
