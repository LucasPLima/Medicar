from django.shortcuts import render
from rest_framework import viewsets
from .models import Agenda
from .serializers import AgendaSerializer

# Create your views here.
class AgendaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
