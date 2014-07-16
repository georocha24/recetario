#encoding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recetario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^receta/(?P<id_receta>\d+)$','principal.views.detalle_receta'),
    url(r'^recetas/$','principal.views.lista_recetas'),
    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^$','principal.views.inicio'),
    url(r'^sobre/$','principal.views.sobre'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    url(r'^contacto/$','principal.views.contacto'),
    url(r'^receta/nueva/$','principal.views.nueva_receta'),
    url(r'^comenta/$','principal.views.nuevo_comentario'),
)
    