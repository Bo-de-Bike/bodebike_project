from django.contrib import admin
from .models import Vacina


class VacinaAdmin(admin.ModelAdmin):
	list_display = ['nome', 'idade']
	search_fields = ['nome', 'idade']
	prepopulated_fields = {'slug':('nome',)}


admin.site.register(Vacina,VacinaAdmin)
