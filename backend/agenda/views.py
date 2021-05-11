from rest_framework import viewsets
from django.db.models import Prefetch
from rest_framework.permissions import IsAuthenticated

from .models import Agenda, Horario
from .serializers import AgendaSerializer
from datetime import date

# Create your views here.
class AgendaViewSet(viewsets.ReadOnlyModelViewSet):
    #.prefetch_related(Prefetch('horarios', queryset=Horario.objects.filter(marcado=False)))
    queryset = Agenda.objects.prefetch_related(Prefetch
                                                (
                                                    'horarios', 
                                                    queryset=Horario.objects.filter(marcado=False))
                                                ).all()
    serializer_class = AgendaSerializer
    permission_classes = [IsAuthenticated]