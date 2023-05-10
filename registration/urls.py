from django.urls import path
from . import views

urlpatterns = [
    path('',views.UserCreateView.as_view(), name='signup'),
    path('verify/',views.VerifyView.as_view(),name='verify'),
]