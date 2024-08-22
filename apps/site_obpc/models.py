from django.db import models
from datetime import datetime,timedelta

class Pastores(models.Model):
    nome_pastor= models.CharField(max_length=100,null=False,blank=False)
    cargo= models.CharField(max_length=100,null=False,blank=False)
    biografia= models.CharField(max_length=2000,null=False,blank=False)
    foto= models.ImageField(upload_to='pastores/foto_pastor',blank=False,help_text="Dimensão: 1051 x 1247 px")
    publicado= models.BooleanField(default=True)
    posicao= models.IntegerField(unique=True,null=True,default=None)

    def __str__(self):
        return self.nome_pastor


class Ministerios(models.Model):
    nome_ministerio=models.CharField(max_length=50,null=False,blank=False)
    descricao_ministerio=models.CharField(max_length=2000,null=False,blank=False)
    foto_ministerio=models.ImageField(upload_to='ministerios/foto_ministerios',help_text="Dimensão: 496 x 388 px")
    logo_ministerio=models.ImageField(upload_to='ministerios/logo_ministerio',help_text="Dimensão: 165 x 48 px")
    card_ministerio = models.ImageField(upload_to='ministerios/card_index',help_text="Dimensão: 320 x 320 px")
    publicado= models.BooleanField(default=True)
    facebook = models.CharField(max_length = 100,null=True, blank = True)
    instagram = models.CharField(max_length = 100,null=True, blank = True)
    email_contato = models.EmailField(null=True,blank=True)
    telefone_contato = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.nome_ministerio

class Lideres_Ministerios(models.Model):
    nome_lider = models.CharField(max_length = 100,null = False, blank = False)
    cargo = models.CharField(max_length = 100,null = False, blank = False)
    ministerio = models.ForeignKey(Ministerios,on_delete=models.CASCADE,default='')
    foto_lider = models.ImageField(upload_to='ministerios/lider_ministerio',help_text="Dimensão: 300 x 250 px")
    posicao = models.IntegerField(null=True,default=None)

    def __str__(self):
        return self.nome_lider
    
class carrosel_index(models.Model):
    nome_imagem = models.CharField(max_length = 50,null=False,blank=False)
    imagem = models.ImageField(upload_to='carrosel',help_text="Dimensão: 1216 x 606 px")
    link_pagina = models.CharField(max_length=50,null=True,blank=True)
    publicado= models.BooleanField(default=True)
    posicao= models.IntegerField(unique=True,null=True,default=None)

    def __str__(self):
        return self.nome_imagem

class Eventos(models.Model):
    nome_evento = models.CharField(max_length=100,null=False,blank=False)
    data_inicio = models.DateField(null=True,blank=True)
    data_fim = models.DateField(null=True,blank=True)
    hora_evento = models.TimeField(null=True)
    Endereco_evento = models.CharField(max_length=200,null=True,blank=True)
    descricao_evento = models.CharField(max_length=2000,null=True,blank=True)
    banner_evento = models.ImageField(upload_to='eventos/banners',help_text="Dimensão: 600 x 600 px")
    foto_card_evento = models.ImageField(upload_to='eventos/card_evento',help_text="Dimensão: 400 x 400 px")
    ministerio = models.ForeignKey(Ministerios, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nome_evento   
    
class Congregacoes(models.Model):
    nome_congregacao = models.CharField(max_length=100, null=False, blank = False)
    descricao_congregacao = models.CharField(max_length=2000,null=True,blank=True)
    facebook = models.CharField(max_length = 100,null=True, blank = True)
    instagram = models.CharField(max_length = 100,null=True, blank = True)
    endereco = models.CharField(max_length = 300,null=True, blank = True)
    link_maps = models.CharField(max_length = 700,null=True, blank = True)
    cultos = models.CharField(max_length = 300,null=True, blank = True)
    foto_banner = models.ImageField(upload_to='congregacoes/banner',help_text="Dimensão: 1415 x 480 px")
    foto_dirigentes = models.ImageField(upload_to='congregacoes/digirentes',help_text="Dimensão: 400 x 480 px")

    def __str__(self):
        return self.nome_congregacao


class Cursos(models.Model):
    nome_curso_extenso = models.CharField(max_length=100, null=False, blank = False)
    nome_curso_abreviado = models.CharField(max_length=100, null=False, blank = False)
    descricao = models.CharField(max_length=5000,null=True,blank=True)
    duracao = models.CharField(max_length=100, null=False, blank = False)
    descricao_duracao = models.CharField(max_length=2000,null=True,blank=True)
    periodo = models.CharField(max_length=100, null=False, blank = False)
    local = models.CharField(max_length=100, null=False, blank = False)
    modalidade = models.CharField(max_length=100, null=False, blank = False)
    investimento = models.CharField(max_length=100, null=False, blank = False)
    descricao_investimento =  models.CharField(max_length=2000,null=True,blank=True)
    informacoes_complementares = models.CharField(max_length=5000,null=True,blank=True)
    nome_coordenacao = models.CharField(max_length=2000,null=True,blank=True)
    foto_coordenacao = models.ImageField(upload_to='cursos/coordenador',help_text="Dimensão: 112 x 112 px")
    foto_banner = models.ImageField(upload_to='cursos/banner',help_text="Dimensão: 330 x 260 px")
    link_inscricao = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.nome_curso_abreviado
    

class Devocional(models.Model):
    titulo_devocional = models.CharField(max_length=100, null=False, blank = False)
    texto_devocional = models.CharField(max_length=10000,null=True,blank=True)
    autor = models.CharField(max_length=100, null=False, blank = False)
    banner_home = models.ImageField(upload_to='devocional/banner',help_text="Dimensão: 1519 x 510 px")
    banner_pagina_devocional = models.ImageField(upload_to='devocional/banner',help_text="Dimensão: 800 x 530 px")
    data_devocional = models.DateField(null=True)

    def __str__(self):
        return self.titulo_devocional
    
class Categoria_servicos(models.Model):
    categoria = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.categoria

class Servicos(models.Model):
    nome_empresa = models.CharField(max_length=100,null=False,blank=False)
    categoria = models.ForeignKey(Categoria_servicos,on_delete=models.CASCADE,default='')
    foto = models.ImageField(upload_to='servicos/foto_empresas',help_text="Dimensão: 380 x 200 px")
    facebook_empresa = models.CharField(max_length=100,null=True,blank=True)
    instagram_empresa = models.CharField(max_length=100,null=True,blank=True)
    whatsapp_empresa = models.CharField(max_length=100,null=True,blank=True)
    site_empresa = models.CharField(max_length=100,null=True,blank=True)
    publicado= models.BooleanField(default=True)

    def __str__(self):
        return self.nome_empresa



class QuemSomos(models.Model):
    nome_qsomos = models.CharField(max_length=100,null=False,blank=False)
    texto = models.CharField(max_length=7000,null=False,blank=False)
    data_publicacao = models.DateField(null=True)

    def __str__(self):
        return self.nome_qsomos