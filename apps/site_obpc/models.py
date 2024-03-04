from django.db import models
from datetime import datetime,timedelta

class Pastores(models.Model):
    nome_pastor= models.CharField(max_length=100,null=False,blank=False)
    cargo= models.CharField(max_length=100,null=False,blank=False)
    biografia= models.CharField(max_length=2000,null=False,blank=False)
    foto= models.ImageField(upload_to='pastores/foto_pastor',blank=False)
    publicado= models.BooleanField(default=True)
    posicao= models.IntegerField(unique=True,null=True,default=None)

    def __str__(self):
        return self.nome_pastor


class Ministerios(models.Model):
    nome_ministerio=models.CharField(max_length=50,null=False,blank=False)
    descricao_ministerio=models.CharField(max_length=2000,null=False,blank=False)
    foto_ministerio=models.ImageField(upload_to='ministerios/foto_ministerios')
    logo_ministerio=models.ImageField(upload_to='ministerios/logo_ministerio')
    card_ministerio = models.ImageField(upload_to='ministerios/card_index')
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
    foto_lider = models.ImageField(upload_to='ministerios/lider_ministerio')
    posicao = models.IntegerField(null=True,default=None)

    def __str__(self):
        return self.nome_lider
    
class carrosel_index(models.Model):
    nome_imagem = models.CharField(max_length = 50,null=False,blank=False)
    imagem = models.ImageField(upload_to='carrosel')
    link_pagina = models.CharField(max_length=50,null=True,blank=True)
    publicado= models.BooleanField(default=True)
    posicao= models.IntegerField(unique=True,null=True,default=None)

    def __str__(self):
        return self.nome_imagem

class Eventos(models.Model):
    nome_evento = models.CharField(max_length=100,null=False,blank=False)
    data_evento = models.DateField(null=True)
    hora_evento = models.TimeField(null=True)
    Endereco_evento = models.CharField(max_length=200,null=True,blank=True)
    descricao_evento = models.CharField(max_length=2000,null=True,blank=True)
    banner_evento = models.ImageField(upload_to='eventos/banners')
    foto_card_evento = models.ImageField(upload_to='eventos/card_evento')
    ministerio = models.ForeignKey(Ministerios, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nome_evento   