from django.db import models
from django.utils import timezone

from medico.models import Medico
from medicar import settings
from datetime import datetime, date
from django.core.exceptions import ValidationError

def format_date(date):
    return date.strftime('%d-%m-%Y')
# Create your models here.
class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)

    def __str__(self):
        return f"Agenda {self.id} - {format_date(self.dia)} | Médico: {self.medico}"
    
    def clean(self):
        def validate_data():
            if self.dia < date.today():
                raise ValidationError({'dia':'Data informada deve ser maior que data atual.'})
        
        def validate_agenda_medico():
            try:
                agenda = Agenda.objects.filter(medico=self.medico, dia=self.dia).get()
                raise ValidationError({'medico':'Médico já contém uma agenda criada nessa data.'})
            except Agenda.DoesNotExist:
                pass

        validate_data()
        validate_agenda_medico()

class Horario(models.Model):
    agenda = models.ForeignKey(Agenda, related_name='horarios', on_delete=models.CASCADE)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    marcado = models.BooleanField(default=False)

    def clean(self):
        def validate_horario_value():
            try:
                horario = Horario.objects.filter(agenda=self.agenda, hora=self.hora).get()
                raise ValidationError({'hora':'Agenda já contém hora informada.'})
            except Horario.DoesNotExist:
                pass
        validate_horario_value()

    def __str__(self):
        return f"Horario: {self.hora} - ({format_date(self.agenda.dia)} - Médico: {self.agenda.medico.nome} | CRM: {self.agenda.medico.crm})"