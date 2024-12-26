from django.shortcuts import render
from productos.forms import SnowboardFormulario
from productos.forms import SkiFormulario
from productos.forms import AntiparrasFormulario
from productos.forms import BuscaAntiparrasForm
from .models import Snowboard, Ski, Antiparras

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request, "productos/inicio.html")

def snowboard(request):
    return render(request, "productos/snowboard.html")

def ski(request):
    return render(request, "productos/ski.html")

def antiparras(request):
    return render(request, "productos/antiparras.html")





def form_Snowboard(request):
    if request.method == "POST":
        mi_formulario = SnowboardFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            snowboard = Snowboard (marca=informacion["marca"], modelo=informacion["modelo"], 
            tamaño=informacion["tamaño"], color=informacion["color"])
            snowboard.save()

            return render(request, "Productos/inicio.html")
    else:
        mi_formulario = SnowboardFormulario()

    return render(request, "Productos/form_Snowboard.html", {"mi_formulario": mi_formulario})



def form_Ski(request):
    if request.method == "POST":
        mi_formulario = SkiFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            ski = Ski (marca=informacion["marca"], modelo=informacion["modelo"], 
            tamaño=informacion["tamaño"], color=informacion["color"])
            ski.save()

            return render(request, "Productos/inicio.html")
    else:
        mi_formulario = SkiFormulario()

    return render(request, "Productos/form_Ski.html", {"mi_formulario": mi_formulario})



def form_Antiparras(request):
    if request.method == "POST":
        mi_formulario = AntiparrasFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            antiparras = Antiparras (marca=informacion["marca"], talle=informacion["talle"],
            modelo=informacion["modelo"], color=informacion["color"])
            antiparras.save()

            return render(request, "Productos/inicio.html")
    else:
        mi_formulario = AntiparrasFormulario()

    return render(request, "Productos/form_Antiparras.html", {"mi_formulario": mi_formulario})



from productos.forms import BuscaAntiparrasForm

def buscar_antiparra(request):
    if request.method == "POST":
        mi_formulario = BuscaAntiparrasForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            list_antiparras = Antiparras.objects.filter(marca__icontains=informacion["marca"])

            return render(request, "productos/resultados_antiparras.html", {"list_antiparras": list_antiparras})
    else:
        mi_formulario = BuscaAntiparrasForm()

    return render(request, "productos/buscar_antiparras.html", {"mi_formulario": mi_formulario})


