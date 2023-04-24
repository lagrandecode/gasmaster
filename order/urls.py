from django.urls import path
from . import views



urlpatterns = [
    path('',views.OrderListView.as_view(),name='order'),
    path('post/',views.OrderListViewPost.as_view(),name='post'),
    path('<int:pk>/',views.OrderDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',views.UpdateStatusView.as_view(),name='update'),
]