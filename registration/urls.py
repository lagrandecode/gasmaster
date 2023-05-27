from django.urls import path
from . import views

urlpatterns = [
    path('user/',views.UserCreateView.as_view(), name='signup'),
    path('add/',views.AdditionView.as_view()),
    path('verify/',views.VerifyView.as_view(),name='verify'),
    path('',views.UserandProfileView.as_view()),
]