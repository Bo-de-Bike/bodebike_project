from django.shortcuts import render
from vacinas.models import Vacina
from doencas.models import Doenca
from core.models import Unidade_de_Vacinacao

def home(request):

	if request.method == 'POST':
		if 'idade' in request.POST:

			context = {}

			context['tipo_de_pesquisa'] = ("Idade : " + request.POST['idade'])

			context['titulo'] = "Vacinas a serem tomadas :"

			vacinas = Vacina.objects.filter(idade=request.POST['idade']) 
			context['listaVacinas'] = vacinas

			unidades = Unidade_de_Vacinacao.objects.all()
			context['unidades_vacinacao'] = unidades

			doencas = Doenca.objects.filter(id_vacina__idade=request.POST['idade'])
			context['doencas'] = doencas

			return render(request,'pesquisa.html', context)

		elif 'doenca' in request.POST:

			context = {'tipo_de_pesquisa':("Tipo de doença : " + request.POST['doenca'])}

			context['titulo'] = "Vacina que trata :"

			unidades = Unidade_de_Vacinacao.objects.all()
			context['unidades_vacinacao'] = unidades

			vacina = Doenca.objects.get(nome=request.POST['doenca'])
			context['tipoVacina'] = vacina


			return render(request,'pesquisa.html', context)

		elif 'vacina' in request.POST:

			context = {'tipo_de_pesquisa':("Tipo de vacina : " + request.POST['vacina'])}

			context['titulo'] = "Doenças que ela trata :"

			vacina = Vacina.objects.get(nome=request.POST['vacina'])
			context['tipoVacina'] = vacina

			unidades = Unidade_de_Vacinacao.objects.all()
			context['unidades_vacinacao'] = unidades

			doencas = Doenca.objects.filter(id_vacina__nome=request.POST['vacina'])
			context['listaDoencas'] = doencas

			return render(request,'pesquisa.html', context)
	
	else:

		context = {}

		vacinas=Vacina.objects.all()
		context['vacinas'] = vacinas

		doencas = Doenca.objects.all()
		context['doencas'] = doencas
		
		return render(request,'home.html',context)

