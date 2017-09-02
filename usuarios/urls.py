from django.conf.urls import url, include
from usuarios.views import RegistrarUsuarioView

urlpatterns = [
    url(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar'),
]