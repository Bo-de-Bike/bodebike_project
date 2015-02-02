from django.contrib import admin
from .models import Unidade_de_Vacinacao


class UnidadesAdmin(admin.ModelAdmin):
	list_display = ['unidade', 'bairro']
	search_fields = ['unidade', 'bairro']

admin.site.register(Unidade_de_Vacinacao,UnidadesAdmin)