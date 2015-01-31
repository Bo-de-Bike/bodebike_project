from django.contrib import admin
from .models import Unidade_de_Vacinacao


class UnidadesAdmin(admin.ModelAdmin):
	list_display = ['unidade', 'endereco']
	search_fields = ['unidade', 'endereco']
	prepopulated_fields = {'slug':('unidade',)}

admin.site.register(Unidade_de_Vacinacao,UnidadesAdmin)