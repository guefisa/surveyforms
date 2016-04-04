from django.conf.urls import url
from django.views.generic.base import TemplateView

from rest_framework.urlpatterns import format_suffix_patterns

from cuestionario import views

urlpatterns = [
	url(r'^respuestas/(?P<pk>[0-9]+)/$', views.RespuestaDetail.as_view()),
    url(r'^preguntas/(?P<pk>[0-9]+)/$', views.PreguntaDetail.as_view()),
    url(r'^preguntas/$', views.PreguntaList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)