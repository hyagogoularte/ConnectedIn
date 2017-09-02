from django.conf.urls import url, include
from django.contrib import admin
from perfis import views as perfis_views

urlpatterns = [
    url(r'^$', perfis_views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', perfis_views.exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', perfis_views.convidar, name='convidar'),
    url(r'^convite/(?P<convite_id>\d+)/aceitar$', perfis_views.aceitar, name='aceitar')

]