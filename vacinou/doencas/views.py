# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404
from doencas.models import Doenca
from vacinas.models import Vacina
def lista(request):
	pass

def detalhes(request,slug):
	context = {}

	doenca = get_object_or_404(Doenca, slug=slug)
	context['doenca'] = doenca

	vacina = Vacina.objects.filter(v_doenca__slug= slug)
	context['tipoVacina'] = vacina
	

	return render(request, 'detalhesDoenca.html', context)
