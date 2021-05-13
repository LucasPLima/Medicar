from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from .models import Consulta, Horario
from .serializers import ConsultaSerializer, ConsultaPostSerializer, ConsultaDestroySerializer

# Create your views here.
class ConsultaViewSet(viewsets.ViewSet):
    permission_classes=[IsAuthenticated]

    def list(self, request):    
        queryset = Consulta.objects.filter(usuario__username=request.user)
        serializer = ConsultaSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ConsultaPostSerializer(data=request.data, context={'request': request})
        data={}
        if serializer.is_valid():
            consulta = serializer.save()
            consulta_qs = Consulta.objects.get(id=consulta.id)
            consulta_serializer = ConsultaSerializer(consulta_qs)
            data = consulta_serializer.data
        else:
            data = serializer.errors

        return Response(data=data)

    def destroy(self, request, pk):
        data = {}
        data['consulta_id'] = pk
        serializer = ConsultaDestroySerializer(data=data, context={'request': request})

        data = {}
        if serializer.is_valid():
            consulta_id = pk
            consulta = Consulta.objects.get(pk=consulta_id, usuario__username= request.user)
        
            up = Horario.objects.filter(pk=consulta.horario.id).update(marcado=False)
            consulta.delete()
        else:
            data = serializer.errors

        return Response(data)