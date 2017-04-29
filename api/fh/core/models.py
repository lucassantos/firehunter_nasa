# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)
    email = models.CharField(max_length=512)
    senha = models.CharField(max_length=8)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __unicode__(self):
        return str(self.nome)


class Foco(models.Model):
    id = models.AutoField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    satelite = models.CharField(max_length=255)
    data_hora_gmt = models.DateTimeField()
    tipo = models.CharField(max_length=256, default='Oficial')

    class Meta:
        verbose_name = "Foco de incendio"
        verbose_name_plural = "Focos de incendios"

    def __unicode__(self):
        return str(self.satelite + "__" + str(self.latitude) + "_" + str(self.longitude))


class Avaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, related_name="Avaliacoes")
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    existeFogo = models.BooleanField(default=True)
    foco = models.ForeignKey(Foco, related_name="Avaliacoes")

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

    def __unicode__(self):
        return str(self.foco.id)+"_"+str(self.usuario.id)+"_"+str(self.existeFogo)


class Denuncia(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, related_name="Denuncias")
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        verbose_name = "Denuncia"
        verbose_name_plural = "Denuncias"

    def __unicode__(self):
        return str(self.foco.id)+"_"+str(self.usuario.id)+"_"+str(self.id)


class FotoDenuncia(models.Model):
    id = models.AutoField(primary_key=True)
    caminho = models.CharField(max_length=1024, blank=True, null=True)
    legenda = models.CharField(max_length=1024, blank=True, null=True)
    denuncia = models.ForeignKey(Denuncia, related_name="Fotos")

    class Meta:
        verbose_name = "Foto de Denuncia"
        verbose_name_plural = "Fotos de Denuncias"

    def __unicode__(self):
        return str(self.legenda)


class FotoAvaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    caminho = models.CharField(max_length=1024, blank=True, null=True)
    legenda = models.CharField(max_length=1024, blank=True, null=True)
    avaliacao = models.ForeignKey(Avaliacao, related_name="Fotos")

    class Meta:
        verbose_name = "Foto de Avaliação"
        verbose_name_plural = "Fotos de Avaliações"

    def __unicode__(self):
        return str(self.legenda)