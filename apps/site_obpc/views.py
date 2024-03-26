from django.shortcuts import render,get_object_or_404
from .models import Pastores,Ministerios,carrosel_index,Eventos,Lideres_Ministerios,Congregacoes,Cursos

def index(request):
    carrosel = carrosel_index.objects.order_by('posicao').filter(publicado=True)
    evento = Eventos.objects.order_by('-data_evento')[:4]
    ministerios = Ministerios.objects.all().filter(publicado=True)
    return render(request,'site/index.html',{"carrosel":carrosel,"evento": evento,"ministerios":ministerios})

def pastores(request):
    pastores= Pastores.objects.order_by('posicao').filter(publicado=True)
    return render(request,'site/pastores.html',{"cards":pastores})

def MinisterioViewSet(request, nome_ministerio):
    ministerio = get_object_or_404(Ministerios, nome_ministerio=nome_ministerio)
    lideres = Lideres_Ministerios.objects.order_by('posicao')
    return render(request, 'site/ministerio.html', {"ministerio": ministerio,"lideres":lideres})

def EventosLista(request):
    evento = Eventos.objects.order_by('-data_evento')
    banner = Eventos.objects.order_by('-data_evento')[0]
    return render(request,'site/eventos.html',{"evento": evento,"banner":banner})

def EventoDetalhe(request, eventos_id):
    evento = get_object_or_404(Eventos, pk=eventos_id)
    eventos = Eventos.objects.all()
    hora_evento = evento.hora_evento.strftime('%I:%M %p')

    if evento.ministerio_id:
        contato = get_object_or_404(Ministerios, pk=evento.ministerio_id)
    else:
        contato = None

    return render(request, 'site/evento.html', {"evento": evento, "eventos": eventos, "hora_evento": hora_evento, "contato": contato})

def CongregacoesViewSet(request,congregacoes_id):
    congregacao = get_object_or_404(Congregacoes,pk=congregacoes_id)
    return render(request,'site/congregacoes.html',{"congregacao":congregacao})

def CursoViewSet(request,curso_id):
    cursos = get_object_or_404(Cursos,pk=curso_id)
    return render(request,'site/cursos.html',{"cursos":cursos})

def ContribuicaoViewSet(request):
    return render(request,'site/contribuicoes.html')