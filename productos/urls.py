from django.urls import path
from productos import views
 
   
urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('snowboard/', views.snowboard, name= "snowboard"),
    path('ski/', views.ski, name= "ski"),
    path('nosotros/', views.nosotros, name= "nosotros"),
    path('antiparras/', views.antiparras, name= "antiparras"),
    path('snowboard-vbc/', views.SnowboardListView.as_view(), name= "ListaSnowboard"),
    path('snowboard-crear', views.SnowboardCreateView.as_view(), name= "CrearSnowboard"),
    path('snowboard-ver/<pk>/', views.SnowboardDetailView.as_view(), name= "VerSnowboard"), 
    path('snowboard-editar/<pk>/', views.SnowboardUpdateView.as_view(), name= "EditarSnowboard"), 
    path('snowboard-confirmar-borrar/<pk>/', views.SnowboardDeleteView.as_view(), name= "BorrarSnowboard") 
]

forms_snowboard = [
    path('form_Snowboard/', views.form_Snowboard, name="FormSnowboard"),
    path('buscar_antiparras/', views.buscar_antiparra, name="BuscarAntiparra")
]

forms_ski = [
    path('form_Ski/', views.form_Ski, name="FormSki")
]

forms_antiparras = [
    path('form_Antiparras/', views.form_Antiparras, name="FormAntiparras")
]

urlpatterns += forms_snowboard + forms_ski + forms_antiparras