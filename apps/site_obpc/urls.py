from django.urls import path
from apps.site_obpc.views import index,pastores,MinisterioViewSet,EventosLista,CongregacoesViewSet,EventoDetalhe

urlpatterns = [
    path('', index,name='index'),
    path('pastores',pastores,name='pastores'),
    path('eventos/',EventosLista,name='eventos'),
    path('eventos/<int:eventos_id>/',EventoDetalhe,name='evento_detalhe'),
    path('ministerios/<str:nome_ministerio>/',MinisterioViewSet,name='ministerio'),
    path('congregacoes',CongregacoesViewSet,name='congregacoes')
]
