from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Agenda
from .serializers import AgendaSerializer
from datetime import date

# Create your views here.
class AgendaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Agenda.objects.filter(dia__gte=date.today()).order_by('dia')
    serializer_class = AgendaSerializer
    permission_classes = [IsAuthenticated]