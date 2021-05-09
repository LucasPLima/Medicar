from agenda.models import Agenda, Horario
from rest_framework import serializers
from medico.serializers import MedicoSerializer
from medicar import settings

class AgendaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()
    horarios = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='hora'
    )
    dia = serializers.DateField(format='%d/%m/%Y', input_formats=settings.DATE_INPUT_FORMATS)
    #horarios = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Agenda
        fields = ['id','medico', 'dia', 'horarios']
