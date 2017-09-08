from django.conf.urls import url, include
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth import views as AuthView

urlpatterns = [
    url(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar'),
    url(r'^login/$', AuthView.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', AuthView.logout_then_login, {'login_url':'/login/'}, name='logout'),
]