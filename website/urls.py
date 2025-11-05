from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), 
    path('listarfuncionarios', views.lista_funcionarios, name='listar_funcionarios'), 
]