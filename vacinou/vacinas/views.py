# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Vacina,Idade
from doencas.models import Doenca

def lista(request):
	pass
def detalhes(request,slug):
	context = {}

	vacina = get_object_or_404(Vacina, slug=slug)
	context['vacina'] = vacina
	#SELECT * FROM vacina V WHERE V.slug = slug

	doencas = Doenca.objects.filter(id_vacina__slug= slug)
	context['doencas'] = doencas
	#SELECT * FROM Doenca D,Vacina V, Doenca_Vacina DV WHERE V.id = DV.id_vacina and D.id = DV.id_doenca and V.slug = slug

	idades = Idade.objects.filter(id_vacina__nome = vacina.nome)
	context['idades'] = idades
	#SELECT * FROM Idade I,Vacina V, Idade_Vacina IV WHERE V.id = IV.id_vacina and D.id = IV.id_idade and V.slug = slug

	return render(request, 'detalhesVacina.html', context)
