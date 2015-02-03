from django.contrib import admin
from .models import Vacina, Idade


class VacinaAdmin(admin.ModelAdmin):
	list_display = ['nome', 'dose']
	search_fields = ['nome']
	prepopulated_fields = {'slug':('nome',)}

class IdadeAdmin(admin.ModelAdmin):
	list_display = ['idade']
	search_fields = ['idade']

admin.site.register(Vacina,VacinaAdmin)
admin.site.register(Idade,IdadeAdmin)

