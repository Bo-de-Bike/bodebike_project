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

	doencas = Doenca.objects.filter(id_vacina__slug= slug)
	context['doencas'] = doencas

	idades = Idade.objects.filter(id_vacina__nome = vacina.nome)
	context['idades'] = idades

	return render(request, 'detalhesVacina.html', context)
