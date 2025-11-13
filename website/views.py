from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from funcionarios.models import Funcionarios
from website.forms import FuncionarioForm
# Create your views here.

def index(request):
    
    return render(request, 'website/index.html')

def lista_funcionarios(request):
    funcionarios = Funcionarios.objects.all()
    contexto = {
        'funcionarios': funcionarios,
        "autor": settings.AUTOR_SISTEMA
    }
    return render(request, 'website/funcionarios.html', contexto)

def detalhes_funcionario(request, id):
    funcionarios = get_object_or_404(Funcionarios, pk=id)
    contexto = {
        "funcionario": funcionarios,
        "autor": settings.AUTOR_SISTEMA}
    return render(request, 'website/detalhesFuncionario.html', contexto)

def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:listar')
    else:
        form = FuncionarioForm()
    return render(request, 'website/cadastrar.html', {'form': form})

def editar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionarios, id=id)

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('website:listar')  # nome da rota que lista funcionários
    else:
        form = FuncionarioForm(instance=funcionario)

    return render(request, 'website/editarfuncionario.html', {'form': form})


def excluir_funcionario(request, id):
    funcionario = get_object_or_404(Funcionarios, pk=id)
    if request.method == "POST":
        funcionario.delete()
        return redirect('website:listar')  
    contexto = {
        "funcionario": funcionario,
        "autor": settings.AUTOR_SISTEMA
        }
    return render(request, 'website/excluir.html', contexto)