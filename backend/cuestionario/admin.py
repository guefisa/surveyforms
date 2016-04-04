# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.html import format_html

from .models import Pregunta, Opcion, Respuesta


# En la administración las opciones se muestran dentro de las preguntas
class OpcionInline(admin.TabularInline):
    model = Opcion
    fk_name = 'pregunta'
    extra = 1

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    fk_name = 'pregunta'
    extra = 1


class PreguntaAdmin(admin.ModelAdmin):
    fields = ('codigo', 'texto', 'orden',)
    list_display = ('codigo', 'texto', 'orden',)
    list_editable = ('orden',)

    inlines = [OpcionInline, RespuestaInline]


admin.site.register(Pregunta, PreguntaAdmin)
