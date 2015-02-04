# -*- coding: utf8 -*-
from django.shortcuts import render
from vacinas.models import Vacina,Idade
from doencas.models import Doenca
from core.models import Unidade_de_Vacinacao,Telefone
from django.db import connection
from core.forms import ContactVacinou



def home(request):

	if request.method == 'POST':

		context = {}

		if 'idade' in request.POST:

			context['tipo_de_pesquisa'] = ("Idade : " + request.POST['idade'])

			context['titulo'] = "Vacinas a serem tomadas :"

			vacinas = Vacina.objects.filter(id_vacina__idade=request.POST['idade']) 
			context['listaVacinas'] = vacinas
			#SELECT * FROM Vacina V,Idade I, Idade_Vacina IV WHERE V.id = IV.id_vacina and I.id = IV.id_vacina and I.idade = request.POST['idade']

			doencas = Doenca.objects.filter(id_vacina__id_vacina__idade = request.POST['idade'])
			context['doencas'] = doencas
			#SELECT * FROM Vacina V,Idade I, Idade_Vacina IV, Doenca_Vacina DV, Doenca D WHERE V.id = IV.id_vacina and I.id = IV.id_vacina and V.id = DV.id_vacina and D.id = DV.id_doenca and I.idade = request.POST['idade']


			unidades = Unidade_de_Vacinacao.objects.all().order_by('bairro')
			context['unidades_vacinacao'] = unidades
			#SELECT * FROM Unidade_de_Vacinacao ORDER BY bairro



		elif 'doenca' in request.POST:

			context = {}

			context['tipo_de_pesquisa'] = ("Tipo de doenca : " + request.POST['doenca'])

			context['titulo'] = "Vacinas que trata :" + request.POST['doenca']

			unidades = Unidade_de_Vacinacao.objects.all().order_by('bairro')
			context['unidades_vacinacao'] = unidades
			#SELECT * FROM Unidade_de_Vacinacao ORDER BY bairro
			
			vacinas = Vacina.objects.filter(v_doenca__nome=request.POST['doenca'])
			context['tipoVacina'] = vacinas
			#SELECT * FROM Vacina V,Doenca D, Doenca_Vacina DV WHERE V.id = DV.id_vacina and D.id = DV.id_doenca and D.nome = request.POST['doenca']

		elif 'vacina' in request.POST:
			context = {}

			context['tipo_de_pesquisa'] = ("Tipo de vacina : " + request.POST['vacina'])

			context['titulo'] = "Doenças que ela trata :"

			idades = Idade.objects.filter(id_vacina__nome=request.POST['vacina'])
			context['idades'] = idades
			#SELECT * FROM Vacina V,Idade I, Idade_Vacina IV WHERE V.id = IV.id_vacina and I.id = IV.id_vacina and V.nome = request.POST['vacina']

			unidades = Unidade_de_Vacinacao.objects.all().order_by('bairro')
			context['unidades_vacinacao'] = unidades
			#SELECT * FROM Unidade_de_Vacinacao ORDER BY bairro

			doencas = Doenca.objects.filter(id_vacina__nome=request.POST['vacina'])
			context['listaDoencas'] = doencas
			#SELECT * FROM Doenca D,Vacina V, Doenca_Vacina DV WHERE V.id = DV.id_vacina and D.id = DV.id_doenca and V.nome = request.POST['vacina']


		form = ContactVacinou(request.POST)
		if form.is_valid():
			print ('sim')
			context['is_valid'] = True
			form.send_mail()
			form = ContactVacinou()
		else:
			print (form.errors)
			form = ContactVacinou()
			print ('nao')
		context['form'] = form


		return render(request,'pesquisa.html', context)

	else:

		context = {}

		idades=Idade.objects.all().order_by('idade')
		context['idades'] = idades
		#SELECT * FROM Idade ORDER BY idade

		vacinas=Vacina.objects.all()
		context['vacinas'] = vacinas
		#SELECT * FROM Vacina 


		doencas = Doenca.objects.all()
		context['doencas'] = doencas
		#SELECT * FROM Doenca

		return render(request,'home.html',context)

