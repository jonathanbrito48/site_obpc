from django.contrib import admin
from django.db import models
from .models import Pastores,Ministerios,carrosel_index,Eventos,Lideres_Ministerios,Congregacoes
from .forms import MinisterioForms, PastoresForms, EventoForms, CongregacaoForms




class PastoresAdmin(admin.ModelAdmin):
    form = PastoresForms
    list_display = ('id', 'posicao','nome_pastor', 'cargo', 'publicado')
    list_display_links = ('id', 'nome_pastor')
    search_fields = ('nome_pastor',)
    list_filter = ('nome_pastor',)
    list_per_page = 10
    list_editable = ('publicado',)

admin.site.register(Pastores, PastoresAdmin)

class MinisteriosAdmin(admin.ModelAdmin):
    form = MinisterioForms
    list_display = ('id','nome_ministerio','publicado')
    list_display_links = ('id','nome_ministerio')
    search_fields = ('nome_ministerio',)
    list_filter = ('nome_ministerio',)
    list_per_page = 10
    list_editable = ('publicado',)

admin.site.register(Ministerios,MinisteriosAdmin)

class CarroselAdmin(admin.ModelAdmin):
    list_display = ('id','nome_imagem','publicado','posicao')
    list_display_links = ('id','nome_imagem')
    search_fields = ('nome_imagem',)
    list_per_page = 10
    list_filter = ('nome_imagem',)
    list_editable = ('publicado',)

admin.site.register(carrosel_index,CarroselAdmin)

class EventosAdmin(admin.ModelAdmin):
    form = EventoForms
    list_display = ('id','nome_evento','data_evento')
    list_display_links = ('nome_evento',)
    search_fields = ('nome_evento','data_evento',)
    list_per_page = 10
    list_filter = ('nome_evento','data_evento',)

admin.site.register(Eventos,EventosAdmin)

class LiredesAdmin(admin.ModelAdmin):
    list_display = ('id','nome_lider','ministerio','posicao')
    list_display_links = ('nome_lider',)
    list_per_page = 10
    list_filter = ('nome_lider','ministerio')

admin.site.register(Lideres_Ministerios,LiredesAdmin)

class CongregacoesAdmin(admin.ModelAdmin):
    form = CongregacaoForms
    list_display = ('id','nome_congregacao')
    list_display_links = ('id','nome_congregacao',)
    list_per_page = 10

admin.site.register(Congregacoes,CongregacoesAdmin)