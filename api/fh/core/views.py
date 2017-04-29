# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.conf import settings
from models import *
import base64
import random
import re


# Create your views here.
class ServiceJson(View):
    @staticmethod
    def Usuarios(request):
        # Query Base
        query = Usuario.objects.all().order_by("nome")

        # Filtros
        nome = request.GET.get("nome")
        id = request.GET.get("id")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)

        lista = serialize('json', query, fields=["id", "nome", "email"])
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    def Focos(request):
        # Query Base
        query = Foco.objects.all()

        # Filtros
        tipo = request.GET.get("tipo")
        id = request.GET.get("id")
        data = request.GET.get("data_hora_gmt")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if data:
            query = query.filter(data_hora_gmt__date=data)

        if (tipo):
            query = query.filter(tipo__icontains=tipo)
        if (id > 0):
            query = query.filter(id=id)

        lista = serialize('json', query, fields=["id", "longitude", "latitude", "satelite", "data_hora_gmt", "tipo"])
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    def Avaliacoes(request):
        # Query Base
        query = Avaliacao.objects.all().order_by("data")

        # Filtros
        usuario_id = request.GET.get("usuario_id")
        foco_id = request.GET.get("foco_id")
        id = request.GET.get("id")
        verdadeiro = request.GET.get("verdadeiro")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (usuario_id):
            query = query.filter(usuario__id=usuario_id)
        if (id > 0):
            query = query.filter(id=id)
        if(foco_id):
            query = query.filter(foco__id=foco_id)
        if(verdadeiro):
            query = query.filter(existeFogo=True)

        lista = serialize('json', query, fields=["id", "data", "usuario__nome", "descricao", "existeFogo", "foco__id"])
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    def Denuncias(request):
        # Query Base
        query = Denuncia.objects.all().order_by("data")
        usuario_id = request.GET.get("usuario_id")
        id = request.GET.get("id")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (usuario_id):
            query = query.filter(usuario__id=usuario_id)
        if (id > 0):
            query = query.filter(id=id)

        lista = serialize('json', query, fields=["id", "data", "usuario__nome", "descricao"])
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def saveusuario(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # Objeto de Usuario
        oUsuario = Usuario()

        if (id):
            if (int(id) > 0):
                oUsuario = Usuario.objects.get(id=id)

        oUsuario.nome = nome
        oUsuario.email = email
        oUsuario.senha = senha

        oUsuario.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    @csrf_exempt
    def savefoco(request):
        # Filtros
        id = request.POST.get("id")
        longitude = request.POST.get("longitude")
        latitude = request.POST.get("latitude")
        satelite = request.POST.get("satelite")
        data_hora_gmt = request.POST.get("data")
        tipo = request.POST.get("tipo")

        # Objeto de Usuario
        oFoco = Foco()
        if (id):
            if (int(id) > 0):
                oFoco = Foco.objects.get(id=id)

        oFoco.longitude = longitude
        oFoco.latitude = latitude
        oFoco.satelite = satelite
        oFoco.data_hora_gmt = data_hora_gmt
        oFoco.tipo = tipo

        oFoco.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    @csrf_exempt
    def saveavaliacao(request):
        # Filtros
        id = request.POST.get("id")
        data = request.POST.get("data")
        usuario_id = request.POST.get("usuario_id")
        descricao = request.POST.get("descricao")
        existefogo = request.POST.get("existefogo")
        foco_id = request.POST.get("foco_id")

        # Objeto de Usuario
        oAvaliacao = Avaliacao()

        if (id):
            if (int(id) > 0):
                oAvaliacao = Avaliacao.objects.get(id=id)

        oAvaliacao.data = data
        oAvaliacao.usuario = Usuario.filter(id=usuario_id).first()
        oAvaliacao.descricao = descricao
        oAvaliacao.existeFogo = bool(existefogo)
        oAvaliacao.foco = Foco.filter(id=foco_id).first()

        oAvaliacao.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    @csrf_exempt
    def savedenuncia(request):
        # Filtros
        id = request.POST.get("id")
        data = request.POST.get("data")
        usuario_id = request.POST.get("usuario_id")
        descricao = request.POST.get("descricao")
        longitude = request.POST.get("longitude")
        latitude = request.POST.get("latitude")

        # Objeto de Usuario
        oDenuncia = Denuncia()

        if (id):
            if (int(id) > 0):
                oDenuncia = Denuncia.objects.get(id=id)

        oDenuncia.data = data
        oDenuncia.usuario = Usuario.filter(id=usuario_id).first()
        oDenuncia.descricao = descricao
        oDenuncia.longitude = longitude
        oDenuncia.latitude = latitude

        oDenuncia.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    @csrf_exempt
    def savefotoDenuncia(request):
        # Filtros
        id = request.POST.get("id")
        foto = request.POST.get("foto")
        legenda = request.POST.get("legenda")
        denuncia_id = request.POST.get("denuncia_id")

        random_n = random.randint(1, 500000000)

        # Objeto de Usuario
        oFotoDenuncia = FotoDenuncia()

        if (id):
            if (int(id) > 0):
                oFotoDenuncia = oFotoDenuncia.objects.get(id=id)

        oFotoDenuncia.legenda = legenda
        oFotoDenuncia.denuncia = Denuncia.filter(id=denuncia_id).first()

        oFotoDenuncia.save()

        filename = str(oFotoDenuncia.id) + '_' + str(random_n) + '.jpg'
        image_data = open(settings.BASE_DIR + '/fh/static/media/denuncia/' + filename, "wb")
        image_data.write(re.sub('^data:image/.+;base64,', '', foto).decode('base64'))
        image_data.close()

        oFotoDenuncia.foto = filename
        oFotoDenuncia.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    @csrf_exempt
    def savefotoAvaliacao(request):
        # Filtros
        id = request.POST.get("id")
        foto = request.POST.get("foto")
        legenda = request.POST.get("legenda")
        avaliacao_id = request.POST.get("avaliacao_id")

        random_n = random.randint(1, 500000000)

        # Objeto de Usuario
        oFotoAvaliacao = FotoAvaliacao()

        if (id):
            if (int(id) > 0):
                oFotoAvaliacao = oFotoAvaliacao.objects.get(id=id)

        oFotoAvaliacao.legenda = legenda
        oFotoAvaliacao.avaliacao = Avaliacao.filter(id=avaliacao_id).first()

        oFotoAvaliacao.save()

        filename = str(oFotoAvaliacao.id) + '_' + str(random_n) + '.jpg'
        image_data = open(settings.BASE_DIR + '/fh/static/media/avaliacao/' + filename, "wb")
        image_data.write(re.sub('^data:image/.+;base64,', '', foto).decode('base64'))
        image_data.close()

        oFotoAvaliacao.foto = filename
        oFotoAvaliacao.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def excluirusuario(request):
        id = request.GET.get("id")

        # Query Base
        oUsuario = Usuario.objects.filter(id=id).first()
        oUsuario.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    def excluirfoco(request):
        id = request.GET.get("id")

        # Query Base
        oFoco = Foco.objects.filter(id=id).first()
        oFoco.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    def excluiravaliacao(request):
        id = request.GET.get("id")

        # Query Base
        oAvaliacao = Avaliacao.objects.filter(id=id).first()
        oAvaliacao.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    def excluirdenuncia(request):
        id = request.GET.get("id")

        # Query Base
        oDenuncia = Denuncia.objects.filter(id=id).first()
        oDenuncia.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    def excluirfotodenuncia(request):
        id = request.GET.get("id")

        # Query Base
        oFotoDenuncia = FotoDenuncia.objects.filter(id=id).first()
        oFotoDenuncia.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')
    @staticmethod
    def excluirfotoavaliacao(request):
        id = request.GET.get("id")

        # Query Base
        oFotoAvaliacao = FotoAvaliacao.objects.filter(id=id).first()
        oFotoAvaliacao.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')