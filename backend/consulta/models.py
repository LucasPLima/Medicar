from django.db import models
from medico.models import Medico
from usuario.models import User

# Create your models here.
class Consulta(models.Model):
    dia = models.DateField(auto_now_add=False, auto_now=False)
    horario = models.TimeField(auto_now_add=False, auto_now=False)
    data_agendamento = models.DateField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    

