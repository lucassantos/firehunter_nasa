"""fh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^js/usuarios', ServiceJson.usuarios, name='usuarios'),
    url(r'^js/focos', ServiceJson.focos, name='focos'),
    url(r'^js/avaliacoes', ServiceJson.avaliacoes, name='avaliacoes'),
    url(r'^js/denuncias', ServiceJson.denuncias, name='denuncias'),

    url(r'^js/saveusuario', ServiceJson.saveusuario, name='saveusuario'),
    url(r'^js/savefoco', ServiceJson.savefoco, name='savefoco'),
    url(r'^js/saveavaliacao', ServiceJson.saveavaliacao, name='saveavaliacao'),
    url(r'^js/savedenuncia', ServiceJson.savedenuncia, name='savedenuncia'),
    url(r'^js/savefotodenuncia', ServiceJson.savefotodenuncia, name='savefotodenuncia'),
    url(r'^js/savefotodenuncia', ServiceJson.savefotodenuncia, name='savefotodenuncia'),

    url(r'^js/excluirusuario', ServiceJson.excluirusuario, name='excluirusuario'),
    url(r'^js/excluirfoco', ServiceJson.excluirfoco, name='excluirfoco'),
    url(r'^js/excluiravaliacao', ServiceJson.excluiravaliacao, name='excluiravaliacao'),
    url(r'^js/excluirdenuncia', ServiceJson.excluirdenuncia, name='excluirdenuncia'),
    url(r'^js/excluirfotodenuncia', ServiceJson.excluirfotodenuncia, name='excluirfotodenuncia'),
    url(r'^js/excluirfotoavaliacao', ServiceJson.excluirfotoavaliacao, name='excluirfotoavaliacao'),
]
