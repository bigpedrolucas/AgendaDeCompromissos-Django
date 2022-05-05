
from django import forms
from django.forms import Textarea
from .models import Compromisso


class formCompromisso(forms.ModelForm):
    class Meta:
        model = Compromisso
        fields = ('titulo', 'observacoes', 'data', 'hora_Inicio', 'hora_Fim', 'local', 'status')
        widgets = {
            'observacoes': Textarea(attrs={'rows': 3}),
            'data': forms.DateInput(attrs={'type':'date'}),
            'hora_Inicio': forms.TimeInput(attrs={'type':'time'}),
            'hora_Fim': forms.TimeInput(attrs={'type':'time'})
        }