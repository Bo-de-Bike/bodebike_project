# -*- coding: utf8 -*-
from django.contrib import admin
from .models import *

class DoencaAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Vacina)
admin.site.register(Doenca,DoencaAdmin)
admin.site.register(Unidade_de_Vacinacao)
