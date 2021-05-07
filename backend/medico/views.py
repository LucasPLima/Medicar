from django.shortcuts import render
from rest_framework import viewsets
from medico.models import Especialidade, Medico
from medico.serializers import MedicoSerializer, EspecialidadeSerializer 

# Create your views here.
class EspecialidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

class MedicoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer