from django.contrib import admin
from .models import Unidade_de_Vacinacao, Telefone


class UnidadesAdmin(admin.ModelAdmin):
	list_display = ['unidade', 'bairro']
	search_fields = ['unidade', 'bairro']

class TelefoneAdmin(admin.ModelAdmin):
	list_display = ['fone']
	search_fields = ['fone']

admin.site.register(Unidade_de_Vacinacao,UnidadesAdmin)
admin.site.register(Telefone,TelefoneAdmin)