from django.conf.urls import url, include
from django.contrib import admin
from perfis import views as perfis_views

urlpatterns = [
    url(r'^$', perfis_views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', perfis_views.exibir, name='exibir')
]