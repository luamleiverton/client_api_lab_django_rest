from rest_framework import serializers
from client.models import Client
from client.validators import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'Formato de CPF inválido'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'Informação de RG deve possuir 9 caracteres'})
        if not phone_valido(data['phone']):
            raise serializers.ValidationError({'phone':'Informação de Phone deve possuir 11 digítos'})
        if not name_valido(data['name']):
            raise serializers.ValidationError({'name':'Somente letras admitido'})
        return data
