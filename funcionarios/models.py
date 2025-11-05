from django.db import models

# Create your models here.

class Funcionarios(models.Model):
    nome = models.CharField(
        max_length=255,
        null = False,
        blank = False
    )

    sobrenome = models.CharField(
        max_length=255,
        null = False,
        blank = False
    )
    
    cpf = models.CharField(
        max_length=14,
        null = False,
        blank = False
    )

    tempo_de_servico = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    remuneracao = models.FloatField(
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
    

    objects = models.Manager()