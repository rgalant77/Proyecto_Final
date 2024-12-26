from django.urls import path
from productos import views
 
   
urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('snowboard/', views.snowboard, name= "snowboard"),
    path('ski/', views.ski, name= "ski"),
    path('antiparras/', views.antiparras, name= "antiparras")
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