from django.shortcuts import render
from productos.forms import SnowboardFormulario
from productos.forms import SkiFormulario
from productos.forms import AntiparrasFormulario
from productos.forms import BuscaAntiparrasForm
from .models import Snowboard, Ski, Antiparras
from productos.forms import BuscaAntiparrasForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request, "productos/inicio.html")

@login_required
def snowboard(request):
    return render(request, "productos/snowboard.html")

@login_required
def ski(request):
    return render(request, "productos/ski.html")

@login_required
def antiparras(request):
    return render(request, "productos/antiparras.html")

def nosotros(request):
    return render(request, "productos/nosotros.html")





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





class SnowboardListView (LoginRequiredMixin, ListView):
    model= Snowboard
    context_object_name= "list_snowboard"
    template_name= "productos/snowboard_lista.html"
    
class SnowboardDetailView (DetailView):
    model= Snowboard
    template_name= "productos/snowboard_detalle.html"
    

class SnowboardCreateView (LoginRequiredMixin, CreateView):
    model= Snowboard
    template_name= "productos/snowboard_crear.html"
    success_url= reverse_lazy ('ListaSnowboard')
    fields = ['marca', 'modelo', 'tamaño', 'color']
    
class SnowboardUpdateView (UpdateView):
    model= Snowboard
    template_name= "productos/snowboard_editar.html"
    success_url= reverse_lazy ('ListaSnowboard')
    fields = ['marca', 'modelo', 'tamaño', 'color']
    
class SnowboardDeleteView (DeleteView):
    model= Snowboard
    template_name= "productos/snowboard_borrar.html"
    success_url= reverse_lazy ('ListaSnowboard')
    
    
    
    