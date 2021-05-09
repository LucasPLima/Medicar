from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Especialidade(models.Model):
    nome = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length= 150)
    crm = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100, unique=True,null=True, blank=True)
    telefone = models.CharField(max_length= 13, null=True, blank=True)
    especialidade = models.ForeignKey(Especialidade, 
                                      on_delete=models.CASCADE)
    
    def clean(self):
        if len(str(self.crm)) != 6:
            raise ValidationError({'crm':'CRM deve conter 6 dígitos.'})

    def __str__(self):
        return f'{self.nome} - CRM: {self.crm} - {self.especialidade}'