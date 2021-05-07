from django.contrib import admin
from .models import Agenda, Horario

# Register your models here.
admin.site.register(Horario)
admin.site.register(Agenda)
