from .models import Ministerios,Pastores,Eventos,Lideres_Ministerios,Congregacoes,Cursos,Devocional,QuemSomos
from django import forms


class MinisterioForms(forms.ModelForm):
    class Meta:
        model =  Ministerios
        fields = '__all__'
        widgets ={
            'descricao_ministerio':forms.Textarea(attrs={'rows':20,'cols':80})
        }

class PastoresForms(forms.ModelForm):
    class Meta:
        model = Pastores
        fields = '__all__'
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 20, 'cols': 80}),
        }

class EventoForms(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = '__all__'
        widgets = {
            'descricao_evento': forms.Textarea(attrs={'rows':20,'cols':80}),
        }

class CongregacaoForms(forms.ModelForm):
    class Meta:
        model = Congregacoes
        fields = '__all__'
        widgets = {
            'cultos': forms.Textarea(attrs={'rows':10,'cols':80}),
            'endereco': forms.Textarea(attrs={'rows':10,'cols':80})
        }

class CursosForms(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = '__all__'
        widgets = {
            'descricao':forms.Textarea(attrs={'rows':20,'cols':80}),
            'descricao_duracao':forms.Textarea(attrs={'rows':10,'cols':80}),
            'descricao_investimento':forms.Textarea(attrs={'rows':10,'cols':80}),
            'informacoes_complementares':forms.Textarea(attrs={'rows':10,'cols':80})
        }

class DevocionalForms(forms.ModelForm):
    class Meta:
        model = Devocional
        fields = '__all__'
        widgets = {
            'texto_devocional':forms.Textarea(attrs={'rows':20,'cols':80})
        }

class Quemsomosform(forms.ModelForm):
    class Meta:
        model = QuemSomos
        fields = '__all__'
        widgets = {
            'texto':forms.Textarea(attrs={'rows':30,'cols':150})
        }
