from django.db import models
from medico.models import Medico
from django.utils import timezone
 
# Create your models here.
class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)

class Horario(models.Model):
    agenda = models.ForeignKey(Agenda, related_name='horarios', on_delete=models.CASCADE)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    marcado = models.BooleanField(default=False)