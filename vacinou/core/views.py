# -*- coding: utf8 -*-
from django.shortcuts import render
from vacinas.models import Vacina,Idade
from doencas.models import Doenca
from core.models import Unidade_de_Vacinacao,Telefone
from django.db import connection




def home(request):

	if request.method == 'POST':
		if 'idade' in request.POST:

			context = {}

			context['tipo_de_pesquisa'] = ("Idade : " + request.POST['idade'])

			context['titulo'] = "Vacinas a serem tomadas :"

			vacinas = Vacina.objects.filter(id_vacina__idade=request.POST['idade']) 
			context['listaVacinas'] = vacinas

			doencas = Doenca.objects.filter(id_vacina__id_vacina__idade = request.POST['idade'])
			context['doencas'] = doencas

			unidades = Unidade_de_Vacinacao.objects.all().order_by('bairro')
			context['unidades_vacinacao'] = unidades



			return render(request,'pesquisa.html', context)

		elif 'doenca' in request.POST:

			context = {'tipo_de_pesquisa':("Tipo de doença : " + request.POST['doenca'])}

			context['titulo'] = "Vacina que trata :"

			unidades = Unidade_de_Vacinacao.objects.all().order_by('bairro')
			context['unidades_vacinacao'] = unidades

			vacinas = Vacina.objects.filter(v_doenca__nome=request.POST['doenca'])
			context['tipoVacina'] = vacinas


			return render(request,'pesquisa.html', context)

		elif 'vacina' in request.POST:
			context = {}

			context['tipo_de_pesquisa'] = ("Tipo de vacina : " + request.POST['vacina'])

			context['titulo'] = "Doenças que ela trata :"

			idades = Idade.objects.filter(id_vacina__nome=request.POST['vacina'])
			context['idades'] = idades

			unidades = Unidade_de_Vacinacao.objects.all().order_by('bairro')
			context['unidades_vacinacao'] = unidades



			doencas = Doenca.objects.filter(id_vacina__nome=request.POST['vacina'])
			context['listaDoencas'] = doencas

			return render(request,'pesquisa.html', context)
	
	else:

		context = {}

		idades=Idade.objects.all().order_by('idade')
		context['idades'] = idades

		vacinas=Vacina.objects.all()
		context['vacinas'] = vacinas

		doencas = Doenca.objects.all()
		context['doencas'] = doencas
		
		return render(request,'home.html',context)

