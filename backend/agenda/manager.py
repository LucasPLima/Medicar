from django.db import models
from datetime import date

class AgendaCustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(dia__gte=date.today(), disponivel=True).order_by('dia')
