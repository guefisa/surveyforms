from rest_framework import serializers

from .models import Pregunta, Opcion, Respuesta


class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ('pk', 'pregunta', 'texto', 'valor', 'salto', 'orden')


class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = ('pk','pregunta','opcion',)


# Serializamos las opciones dentro de las preguntas
class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many=True, read_only=True)
    respuestas = RespuestaSerializer(many=True, read_only=True)

    class Meta:
        model = Pregunta
        fields = ('pk', 'codigo', 'texto', 'opciones', 'respuestas', 'orden',)