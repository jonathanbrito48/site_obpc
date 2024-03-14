from .models import Ministerios, Congregacoes

def MinisteriosContext(request):
    return{"ministerios":Ministerios.objects.all()}

def CongregacoesContext(request):
    return{"congregacoes":Congregacoes.objects.all()}