from django.urls import path
from apps.site_obpc.views import index,pastores,umasbrac,ufebrac

urlpatterns = [
    path('', index,name='index'),
    path('pastores',pastores,name='pastores'),
    path('umasbrac',umasbrac,name='umasbrac'),
    path('ufebrac',ufebrac,name='ufebrac')
]
