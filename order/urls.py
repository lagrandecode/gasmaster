from django.urls import path
from . import views



urlpatterns = [
    path('',views.OrderListView.as_view(),name='order'),
    path('post/',views.OrderListViewPost.as_view(),name='post'),
]