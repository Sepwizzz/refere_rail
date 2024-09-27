from rest_framework import serializers
from .models import Arbitros, Organizador,Evento

class ArbitrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arbitros
        fields = '__all__'

class OrganizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizador
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = '__all__'