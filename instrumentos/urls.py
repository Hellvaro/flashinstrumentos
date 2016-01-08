from django.conf.urls import patterns, include, url

from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'instrumentos.views.home', name='home'),
    # url(r'^instrumentos/', include('instrumentos.foo.urls')),
    url(r'^registrar/$', registrarPublicacion.as_view(), name= "registrar_publicacion"),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^publicacion/', include('principal.urls')),
    
)
