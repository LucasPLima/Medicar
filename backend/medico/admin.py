from django.contrib import admin
from .models import Medico, Especialidade

class MedicoAdmin(admin.ModelAdmin):
    list_display=('nome','crm','email','especialidade')
    list_filter=('especialidade',)

# Register your models here.
admin.site.register(Especialidade)
admin.site.register(Medico, MedicoAdmin)