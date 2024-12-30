from .models import Ministerios, Congregacoes,Cursos

def MinisteriosContext(request):
    return{"ministerios":Ministerios.objects.all()}

def CongregacoesContext(request):
    return{"congregacoes":Congregacoes.objects.all()}

def CursosContext(request):
    return{"cursos_menu":Cursos.objects.order_by('nome_curso_abreviado')}