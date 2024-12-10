from django import forms
from .models import Seguro

class SeguroForm(forms.ModelForm):
    class Meta:
        model = Seguro
        fields = ['tipo', 'archivo']
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de Seguro'}),
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
