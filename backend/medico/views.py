from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from .models import Especialidade, Medico
from .serializers import MedicoSerializer, EspecialidadeSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EspecialidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    permission_classes =[IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']
class MedicoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes =[IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nome', ]
    filterset_fields = ['especialidade']
    