from django.urls import path
from . import views

app_name = 'operaciones'

urlpatterns = [
    # Menú principal de Actividad 3: /operaciones/
    path('', views.index, name='index'),
    # Tarea 1: Operaciones matemáticas
    path('calculadora/', views.calculadora_form, name='calculadora_form'),
    path('calculadora/resultado/', views.calculadora_resultado, name='calculadora_resultado'),
    # Tarea 2: Volumen de un cilindro
    path('cilindro/', views.cilindro_vista, name='cilindro'),
]
