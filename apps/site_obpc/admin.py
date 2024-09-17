from django.contrib import admin
from django.db import models
from .models import Pastores,Ministerios,carrosel_index,Eventos,Lideres_Ministerios,Congregacoes,Cursos,Devocional,Servicos,Categoria_servicos,QuemSomos,InstagramToken,Instagramapi
from .forms import MinisterioForms, PastoresForms, EventoForms, CongregacaoForms, CursosForms,DevocionalForms,Quemsomosform




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
    list_display = ('id','nome_evento','data_inicio')
    list_display_links = ('nome_evento',)
    search_fields = ('nome_evento','data_inicio',)
    list_per_page = 10
    list_filter = ('nome_evento','data_inicio',)

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

class CursosAdmin(admin.ModelAdmin):
    form = CursosForms
    list_display = ('id','nome_curso_extenso')
    list_display_links = ('id','nome_curso_extenso',)
    list_per_page = 10

admin.site.register(Cursos,CursosAdmin)

class DevocionalAdmin(admin.ModelAdmin):
    form = DevocionalForms
    list_display = ('id','titulo_devocional','data_devocional')
    list_display_links = ('id','titulo_devocional','data_devocional',)
    list_per_page = 10
    list_filter = ('autor','data_devocional',)

admin.site.register(Devocional,DevocionalAdmin)

class ServicosAdmin(admin.ModelAdmin):
    list_display = ('id','nome_empresa','categoria','publicado')
    list_display_links = ('id','nome_empresa',)
    list_editable = ('publicado',)
    list_per_page = 10
    list_filter = ('categoria','publicado',)

admin.site.register(Servicos,ServicosAdmin)

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id','categoria')
    list_display_links = ('id','categoria')

admin.site.register(Categoria_servicos,CategoriasAdmin)

class QuemsomosAdmin(admin.ModelAdmin):
    form = Quemsomosform
    list_display = ('id','nome_qsomos','data_publicacao')
    list_display_links = ('id','nome_qsomos',)
    list_per_page = 20

admin.site.register(QuemSomos,QuemsomosAdmin)

class InstagramTokenAdmin(admin.ModelAdmin):
    list_display = ('id','token')
    list_display_links = ('id','token',)

admin.site.register(InstagramToken,InstagramTokenAdmin)

class InstagramIndexAdmin(admin.ModelAdmin):
    list_display= ('id_instagram','timestamp','media_type','created_time')
    list_display_links = ('id_instagram','media_type','timestamp',)

admin.site.register(Instagramapi,InstagramIndexAdmin)
