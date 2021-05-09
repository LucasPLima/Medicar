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

    def validate(self, data):
        def validate_agenda(data):
            try:
                agenda = Agenda.objects.get(id=data['agenda_id'])
                if agenda.dia < date.today():
                    raise serializers.ValidationError({'agenda':'Data da agenda indicada anterior a data atual!'})

            except Agenda.DoesNotExist:
                raise serializers.ValidationError({'agenda':'Agenda solicitada inexistente!'})

        def validate_horario(data):
            try:
                horario = Horario.objects.get(agenda__id=data['agenda_id'], hora=data['horario'])
                if horario.marcado == True:
                    raise serializers.ValidationError({'horario':'Horário solicitado já foi marcado!'})    
            except Horario.DoesNotExist:
                raise serializers.ValidationError({'horario':'Horário solicitado não existe!'})
        
        validate_agenda(data)
        validate_horario(data)
        return data

    def save(self):
        agenda_id = self.validated_data['agenda_id']
        horario = self.validated_data['horario']
        
        agenda = Agenda.objects.get(id=agenda_id)
        medico = agenda.medico
        dia = agenda.dia

        usuario= User.objects.get(username=self.context['request'].user)

        consulta= Consulta(dia=dia, horario=horario, medico=medico, usuario=usuario)
        up = Horario.objects.filter(agenda__id=agenda_id, hora=horario).update(marcado=True)
        consulta.save()
        
        return consulta


        
        

