# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Vacina
from doencas.models import Doenca

def lista(request):
	pass
def detalhes(request,slug):
	context = {}

	vacina = get_object_or_404(Vacina, slug=slug)
	context['vacina'] = vacina

	doencas = Doenca.objects.filter(id_vacina__nome=vacina)
	context['doencas'] = doencas

	return render(request, 'detalhesVacina.html', context)
