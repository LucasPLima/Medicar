from rest_framework import viewsets
from django.db.models import Prefetch, OuterRef, Exists
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Agenda, Horario
from .serializers import AgendaSerializer
# Create your views here.
class AgendaViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['medico']

    def list(self, request):
      horarios_desmarcados = Horario.objects.disponiveis().filter(agenda=OuterRef('pk'))

      queryset = Agenda.objects.disponiveis().prefetch_related(
                                              Prefetch
                                                  ('horarios', 
                                                    queryset=Horario.objects.disponiveis())
                                                  ).filter(Exists(horarios_desmarcados))
      serializer = AgendaSerializer(queryset, many=True)
      return Response(serializer.data)
      