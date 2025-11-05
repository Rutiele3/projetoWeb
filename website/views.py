from django.shortcuts import render
from funcionarios.models import Funcionarios
# Create your views here.

def index(request):
    
    return render(request, 'website/index.html')

def lista_funcionarios(request):
    funcionarios = Funcionarios.objects.all()
    contexto = {
        'funcionarios': funcionarios
    }
    return render(request, 'website/listarfuncionarios.html', contexto)