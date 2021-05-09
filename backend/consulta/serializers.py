from .models import Consulta
from usuario.models import User
from agenda.models import Agenda, Horario
from datetime import date

from medico.serializers import MedicoSerializer
from rest_framework import serializers


class ConsultaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()

    class Meta:
        model = Consulta
        fields = ['id','dia','horario','data_agendamento','medico']
    

class ConsultaPostSerializer(serializers.Serializer):
    agenda_id = serializers.IntegerField()
    horario = serializers.TimeField()

    def validate(self, obj):
        def validate_agenda(obj):
            try:
                agenda = Agenda.objects.get(id=obj['agenda_id'])
                if agenda.dia < date.today():
                    raise serializers.ValidationError({'agenda':'Data da agenda indicada anterior a data atual!'})

            except Agenda.DoesNotExist:
                raise serializers.ValidationError({'agenda':'Agenda solicitada inexistente!'})

        def validate_horario(obj):
            try:
                horario = Horario.objects.get(agenda__id=obj['agenda_id'], hora=obj['horario'])
                if horario.marcado == True:
                    raise serializers.ValidationError({'horario':'Horário solicitado já foi marcado!'})    
            except Horario.DoesNotExist:
                raise serializers.ValidationError({'horario':'Horário solicitado não existe!'})
        
        validate_agenda(obj)
        validate_horario(obj)
        return obj

    def save(self):
        agenda_id = self.validated_data['agenda_id']
        horario = self.validated_data['horario']
        
        agenda = Agenda.objects.get(id=agenda_id)
        medico = agenda.medico
        dia = agenda.dia
        usuario= User.objects.get(username='lucas2')

        consulta= Consulta(dia=dia, horario=horario, medico=medico, usuario=usuario)
        up = Horario.objects.filter(agenda__id=agenda_id, hora=horario).update(marcado=True)
        consulta.save()
        
        return consulta


        
        

