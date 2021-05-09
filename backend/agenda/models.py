from django.db import models
from medico.models import Medico
from django.utils import timezone
from medicar import settings
from datetime import datetime

def format_date(date):
    return date.strftime('%d-%m-%Y')
# Create your models here.
class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)

    def __str__(self):
        return f"Agenda {self.id} - {format_date(self.dia)} | Médico: {self.medico}"

class Horario(models.Model):
    agenda = models.ForeignKey(Agenda, related_name='horarios', on_delete=models.CASCADE)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    marcado = models.BooleanField(default=False)

    def __str__(self):
        return f"Horario: {self.hora} - ({format_date(self.agenda.dia)} - Médico: {self.agenda.medico.nome} | CRM: {self.agenda.medico.crm})"