from .models import Consulta
from usuario.models import User
from agenda.models import Agenda, Horario
from datetime import date, datetime
from django.utils import timezone

from medico.serializers import MedicoSerializer
from rest_framework import serializers


class ConsultaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()
    dia =  serializers.DateField(source='agenda.dia', format='%d/%m/%Y')
    horario = serializers.TimeField(source='horario.hora')
    data_agendamento = serializers.DateField(format='%d/%m/%Y')
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
        horario_req = self.validated_data['horario']
        
        agenda = Agenda.objects.get(id=agenda_id)
        medico = agenda.medico
        
        horario = Horario.objects.get(agenda__id=agenda_id, hora=horario_req)
        usuario = User.objects.get(username=self.context['request'].user)

        consulta= Consulta(agenda=agenda, horario=horario, medico=medico, usuario=usuario)
        up = Horario.objects.filter(pk=horario.id).update(marcado=True)
        consulta.save()
        
        return consulta


class ConsultaDestroySerializer(serializers.Serializer):
    consulta_id = serializers.IntegerField()

    def validate(self, data):
        try:
            horario_atual = datetime.now().time()
            consulta = Consulta.objects.get(pk=data['consulta_id'], usuario__username=self.context['request'].user)

            if consulta.agenda.dia == date.today():
                if consulta.horario.hora < horario_atual:
                    raise serializers.ValidationError({'consulta':'Não é possível desmarcar uma consulta que já aconteceu!'})
            elif  consulta.agenda.dia < date.today():
                raise serializers.ValidationError({'consulta':'Não é possível desmarcar uma consulta que já aconteceu!'})

            return data    

        except Consulta.DoesNotExist:
            raise serializers.ValidationError({'consulta':'Consulta inexistente ou não cadastrada para este usuário!'})
        

