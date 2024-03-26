from django.urls import path
from apps.site_obpc.views import index,pastores,MinisterioViewSet,EventosLista,CongregacoesViewSet,EventoDetalhe,CursoViewSet,ContribuicaoViewSet

urlpatterns = [
    path('', index,name='index'),
    path('pastores',pastores,name='pastores'),
    path('eventos/',EventosLista,name='eventos'),
    path('eventos/<int:eventos_id>/',EventoDetalhe,name='evento_detalhe'),
    path('ministerios/<str:nome_ministerio>/',MinisterioViewSet,name='ministerio'),
    path('congregacoes/<int:congregacoes_id>/',CongregacoesViewSet,name='congregacoes'),
    path('cursos/<int:curso_id>/',CursoViewSet,name='cursos'),
    path('contribuicoes',ContribuicaoViewSet,name='contribuicoes')
]
