from django.db import models
from datetime import date, datetime
from django.utils import timezone
from django.db.models import  Q

class AgendaCustomManager(models.Manager):
    def disponiveis(self):
        return super().get_queryset().filter(dia__gte=date.today()).order_by('dia')

class HorarioCustomManager(models.Manager):
    def disponiveis(self):
        hora_atual = timezone.localtime(timezone.now())
        hora_padrao = datetime.strptime('00:00', '%H:%M')
        
        return super().get_queryset().filter(
                                (
                                  Q(agenda__dia=date.today(), 
                                   hora__gte=hora_atual) 
                                  | Q(agenda__dia__gt=date.today(),
                                    hora__gte=hora_padrao)
                                ), 
                                marcado=False
                                ).order_by('hora')
                                
