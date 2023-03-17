

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static


urlpatterns = [
    path('',views.api_list),
    path('',views.product_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
