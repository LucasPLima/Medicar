from medico.models import Especialidade, Medico
from rest_framework import serializers


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ['id','nome']

class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializer()
    
    class Meta:
        model = Medico
        fields = ['id','crm', 'nome', 'email','telefone', 'especialidade']
   
    