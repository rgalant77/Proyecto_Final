from django import forms

class SnowboardFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    tamaño = forms.IntegerField()
    color = forms.CharField()
    
class SkiFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    tamaño = forms.IntegerField()
    color = forms.CharField()
    
class AntiparrasFormulario(forms.Form):
    marca = forms.CharField()
    talle = forms.IntegerField()
    modelo = forms.CharField()
    color = forms.CharField()
    
    
class BuscaAntiparrasForm (forms.Form):
    marca = forms.CharField()