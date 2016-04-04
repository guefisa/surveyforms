# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import loader
from rest_framework import generics

from .models import Pregunta, Respuesta
from .serializers import PreguntaSerializer, RespuestaSerializer

'''
Estas clases genericas contruyen nuestra API y
nos proporcionan una interfaz web para navegar por ella.
'''
class PreguntaList(generics.ListCreateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class PreguntaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class RespuestaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer