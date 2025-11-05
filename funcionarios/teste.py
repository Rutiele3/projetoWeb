from funcionarios.models import Funcionarios

 # Criar e salvar um novo funcionário
funcionarios = Funcionarios(
     nome='Rutiele',
     sobrenome='de Souza Favela',
     cpf='123.456.789-00',
     tempo_de_servico=4,
     remuneracao=18000.00
)
funcionarios.save()

funcionarios = Funcionarios(
     nome='Ruti',
     sobrenome='Favela',
     cpf='123.456.789-00',
     tempo_de_servico=6,
     remuneracao=1500.00
)

funcionarios.save()

#print("Funcionário salvo com sucesso:", funcionarios.nome, funcionarios.sobrenome)

#funcionario = Funcionarios.objetos.get(id=1)

#funcipnarios = Funcionarios.objetos.exclude(nome="Rutiele").filter(tempo_de_servico__gt=3).filter(remuneracao__lt=5000).all()

#funcionarios = Funcionarios.objetos.first(tempo_de_servico__gt=3).all()"""

#print(funcionarios.id)




# Primeiro, encontramos o Funcionário que desejamos deletar
#funcionario = Funcionarios.objetos.get(id=1)
# Agora, o deletamos!
#
# 
# 
# funcionarios.delete()




# Primeiro, encontramos o Funcionário que desejamos deletar
funcionarios = Funcionarios.objetos.get(id=20)
# Agora, o deletamos!
funcionarios.delete()


# Primeiro, buscamos o funcionário desejado
funcionarios = Funcionarios.objetos.get(id=21)
# Alteramos seu sobrenome
funcionarios.sobrenome = f"{funcionarios.sobrenome} Albuquerque"
# Salvamos as alterações
funcionarios.save()
