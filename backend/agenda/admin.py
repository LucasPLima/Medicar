from django.contrib import admin
from .models import Agenda, Horario

class AgendaAdmin(admin.ModelAdmin):
    list_display=('dia','medico')
    list_filter=('dia','medico')

class HorarioAdmin(admin.ModelAdmin):
    list_display=('agenda','hora','marcado')
    list_filter=('agenda',)

# Register your models here.
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Agenda, AgendaAdmin)
