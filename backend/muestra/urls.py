from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from muestra import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^muestras/$', views.MuestraList.as_view(), name='muestra-list'),
    url(r'^muestras/(?P<pk>[0-9]+)/$', views.MuestraDetail.as_view(), name='muestra-detail'),    
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='muestra-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)