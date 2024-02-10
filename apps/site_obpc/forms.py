from .models import Ministerios,Pastores,Eventos,Lideres_Ministerios
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






