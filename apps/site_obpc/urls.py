from django.urls import path
from apps.site_obpc.views import index

urlpatterns = [
    path('', index,name='index'),
]
