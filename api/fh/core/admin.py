# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import *

admin.site.register(Usuario)
admin.site.register(Denuncia)
admin.site.register(Foco)
admin.site.register(Avaliacao)
admin.site.register(FotoAvaliacao)
admin.site.register(FotoDenuncia)