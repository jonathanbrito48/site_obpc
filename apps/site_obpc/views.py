from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from .models import Pastores,Ministerios,carrosel_index,Eventos,Lideres_Ministerios\
    ,Congregacoes,Cursos,Devocional,Servicos,Categoria_servicos,QuemSomos,InstagramToken
from django.utils import timezone
from django.db.models import Count,Q
import requests
from django.conf import settings

def index(request):
    carrosel = carrosel_index.objects.order_by('posicao').filter(publicado=True)
    evento = Eventos.objects.filter(
        Q(data_inicio__gte=timezone.now()) | Q(data_fim__gte=timezone.now())
        ).order_by('data_inicio')[:3]
    ministerios = Ministerios.objects.all().filter(publicado=True)
    devocional = Devocional.objects.order_by('-data_devocional')[:1]
    congregacoes = Congregacoes.objects.all()

    access_token = InstagramToken.objects.all()[0]
    url = f"https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,children&access_token={access_token}"
    response = requests.get(url)
    data = response.json()

    posts = []
    for media in data.get('data', []):
        if media['media_type'] == 'CAROUSEL_ALBUM':
            carousel_id = media['id']
            carousel_url = f"https://graph.instagram.com/{carousel_id}?fields=children{{media_type,media_url,thumbnail_url}}&access_token={access_token}"
            carousel_response = requests.get(carousel_url)
            carousel_data = carousel_response.json()
            children = carousel_data.get('children', {}).get('data', [])
            if children:
                first_child = children[0]
                posts.append({
                    'media_type': first_child['media_type'],
                    'media_url': first_child['media_url'],
                    'permalink': media.get('permalink'),
                    'caption': media.get('caption'),
                    'thumbnail_url':media.get('thumbnail_url')
                })
        else:
            posts.append({
                'media_type': media.get('media_type'),
                'media_url': media.get('media_url'),
                'permalink': media.get('permalink'),
                'caption': media.get('caption'),
                'thumbnail_url':media.get('thumbnail_url')
            })
    posts = posts[:15]
    context = {
        "posts": posts,"congregacoes":congregacoes,"carrosel":carrosel,"evento": evento,"ministerios":ministerios,"devocional":devocional
    }

    return render(request,'site/index.html',context)

def pastores(request):
    pastores= Pastores.objects.order_by('posicao').filter(publicado=True)
    return render(request,'site/pastores.html',{"cards":pastores})

def MinisterioViewSet(request, nome_ministerio):
    ministerio = get_object_or_404(Ministerios, nome_ministerio=nome_ministerio)
    lideres = Lideres_Ministerios.objects.order_by('posicao')
    return render(request, 'site/ministerio.html', {"ministerio": ministerio,"lideres":lideres})

def EventosLista(request):
    evento = Eventos.objects.filter(data_inicio__gte=timezone.now()).order_by('data_inicio')
    banner = Eventos.objects.order_by('-data_inicio')[0]
    paginator = Paginator(evento,10)

    page = request.GET.get('page')
    try:
        eventos_pagina = paginator.page(page)
    except PageNotAnInteger:
        eventos_pagina = paginator.page(1)
    except EmptyPage:
        eventos_pagina = paginator.page(paginator.num_pages)
    return render(request,'site/eventos.html',{"banner":banner,"eventos_pagina":eventos_pagina})

def EventoDetalhe(request, eventos_id):
    evento = get_object_or_404(Eventos, pk=eventos_id)
    eventos = Eventos.objects.all()
    hora_evento = evento.hora_evento.strftime('%I:%M %p')

    if evento.ministerio_id:
        contato = get_object_or_404(Ministerios, pk=evento.ministerio_id)
    else:
        contato = None

    mais_eventos =  Eventos.objects.filter(data_inicio__gte=timezone.now()).order_by('data_inicio')[:4]

    return render(request, 'site/evento.html', {"evento": evento, "eventos": eventos, "hora_evento": hora_evento, "contato": contato,"mais_eventos":mais_eventos})

def CongregacoesViewSet(request,congregacoes_id):
    congregacao = get_object_or_404(Congregacoes,pk=congregacoes_id)
    return render(request,'site/congregacoes.html',{"congregacao":congregacao})

def CursoViewSet(request,curso_id):
    cursos = get_object_or_404(Cursos,pk=curso_id)
    return render(request,'site/cursos.html',{"cursos":cursos})

def ContribuicaoViewSet(request):
    return render(request,'site/contribuicoes.html')

def quemsomosViewSet(request):
    quemsomos = QuemSomos.objects.order_by('data_publicacao')[0]
    return render(request,'site/quemsomos.html',{'quemsomos':quemsomos})

def DevocionalViewSet(request):
    devocionais = Devocional.objects.order_by('-data_devocional')

    paginator = Paginator(devocionais,5)

    page = request.GET.get('page')
    try:
        devocionais_pagina = paginator.page(page)
    except PageNotAnInteger:
        devocionais_pagina = paginator.page(1)
    except EmptyPage:
        devocionais_pagina = paginator.page(paginator.num_pages)
    return render(request,'site/devocionais.html',{"devocionais":devocionais,"devocionais_pagina":devocionais_pagina})

def DevocionalDetalheViewSet(request, devocional_id):
    devocional = get_object_or_404(Devocional, pk=devocional_id)
    devocionais = Devocional.objects.all()
    mais_devocionais = Devocional.objects.order_by('-data_devocional')[:6]

    return render(request, 'site/devocional.html', {"devocional": devocional, "devocionais": devocionais,"mais_devocionais":mais_devocionais})

def divulgacao_servicos_view(request):
    categorias = Categoria_servicos.objects.annotate(num_servicos=Count('servicos')).filter(num_servicos__gt=0)
    categoria_selecionada = request.GET.get('categoria')

    if categoria_selecionada:
        servicos = Servicos.objects.filter(categoria_id=categoria_selecionada).filter(publicado=True).order_by('categoria')
    else:
        servicos = Servicos.objects.all().filter(publicado=True).order_by('categoria')

    paginator = Paginator(servicos,9)

    page = request.GET.get('page')
    try:
        servicos_pagina = paginator.page(page)
    except PageNotAnInteger:
        servicos_pagina = paginator.page(1)
    except EmptyPage:
        servicos_pagina = paginator.page(paginator.num_pages)

    context = {
        'categorias': categorias,
        'servicos': servicos,
        'categoria_selecionada': categoria_selecionada,
        'servicos_pagina':servicos_pagina,
    }
    return render(request,'site/divulgacao_servicos.html',context)
