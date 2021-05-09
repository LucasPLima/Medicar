from django.shortcuts import render
from rest_framework import viewsets
from .models import Especialidade, Medico
from .serializers import MedicoSerializer, EspecialidadeSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EspecialidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

class MedicoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes =[IsAuthenticated]