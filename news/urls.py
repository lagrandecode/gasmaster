from django.urls import path
from . import views



urlpatterns = [
    path('',views.GasNewsList.as_view(),name='news'),
]