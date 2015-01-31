from django.contrib import admin
from .models import Doenca

class DoencaAdmin(admin.ModelAdmin):
	list_display = ['nome', 'slug']
	search_fields = ['nome', 'slug']
	prepopulated_fields = {'slug':('nome',)}

admin.site.register(Doenca,DoencaAdmin)
