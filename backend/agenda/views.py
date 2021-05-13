from rest_framework import viewsets
from django.db.models import Prefetch, OuterRef, Exists
from rest_framework.permissions import IsAuthenticated

from .models import Agenda, Horario
from .serializers import AgendaSerializer
from django.utils import timezone
from datetime import date
# Create your views here.
class AgendaViewSet(viewsets.ReadOnlyModelViewSet):
    horarios_desmarcados = Horario.objects.disponiveis().filter(agenda=OuterRef('pk'), marcado=False)

    queryset = Agenda.objects.disponiveis().prefetch_related(
                                            Prefetch
                                                ('horarios', 
                                                  queryset=Horario.objects.disponiveis())
                                                ).filter(Exists(horarios_desmarcados))
    serializer_class = AgendaSerializer
    permission_classes = [IsAuthenticated]