from django.contrib import admin
from .models import Medico, Especialidade
# Register your models here.

admin.site.register(Especialidade)
admin.site.register(Medico)