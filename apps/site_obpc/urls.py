from django.urls import path
from apps.site_obpc.views import index,pastores,MinisterioViewSet,EventosLista,\
    CongregacoesViewSet,EventoDetalhe,CursoViewSet,ContribuicaoViewSet,quemsomosViewSet,\
    DevocionalViewSet,DevocionalDetalheViewSet,divulgacao_servicos_view

urlpatterns = [
    path('', index,name='index'),
    path('pastores',pastores,name='pastores'),
    path('eventos/',EventosLista,name='eventos'),
    path('eventos/<int:eventos_id>/',EventoDetalhe,name='evento_detalhe'),
    path('ministerios/<str:nome_ministerio>/',MinisterioViewSet,name='ministerio'),
    path('cursos/<int:curso_id>/',CursoViewSet,name='cursos'),
    path('contribuicoes',ContribuicaoViewSet,name='contribuicoes'),
    path('quemsomos',quemsomosViewSet,name='quemsomos'),
    path('devocionais/',DevocionalViewSet,name='devocionais'),
    path('devocionais/<int:devocional_id>/',DevocionalDetalheViewSet,name='devocional_detalhe'),
    path('servicos',divulgacao_servicos_view,name='servicos'),
    path('quemsomos',quemsomosViewSet,name='quemsomos')
]
