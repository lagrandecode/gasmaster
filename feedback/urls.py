from django.urls import path
from . import views

urlpatterns = [
    path('',views.FeedbackView.as_view(),name='feedback'),
    path('<int:pk>/',views.FeedbackDetailView.as_view()),
]