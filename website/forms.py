# funcionarios/forms.py
from django import forms
from funcionarios.models import Funcionarios

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['nome', 'remuneracao', 'sobrenome', 'cpf', 'tempo_de_servico']
