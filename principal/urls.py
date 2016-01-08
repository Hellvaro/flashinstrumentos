from django.conf.urls import patterns, include, url
from .views import registrarPublicacion

urlpatterns = patterns('',
    url(r'^registrar/$', registrarPublicacion.as_view(), name= "registrar_publicacion"),
      url(r'^registrar/$', ReportarPublicacion.as_view(), name= "reportar_publicacion"),
)

