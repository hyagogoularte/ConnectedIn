from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite

def index(request):
    perfis_obj = Perfil.objects.all()
    perfil_logado_obj = get_perfil_logado(request)
    return render(request, 'index.html', {"perfis": perfis_obj, "perfil_logado": perfil_logado_obj})

def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    
    perfil_logado_obj = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado_obj.contatos.all()
    
    return render(request, 'perfil.html', {"perfil": perfil, "ja_eh_contato": ja_eh_contato})

def convidar(request, perfil_id):
    perfil_a_convidar_obj = Perfil.objects.get(id=perfil_id)
    perfil_logado_obj = get_perfil_logado(request)
    perfil_logado_obj.convidar(perfil_a_convidar_obj)
    return redirect('index')

def aceitar(request, convite_id):
    convite_obj = Convite.objects.get(id=convite_id)
    convite_obj.aceitar()
    return redirect('index')

def get_perfil_logado(request):
    return Perfil.objects.get(id=1)