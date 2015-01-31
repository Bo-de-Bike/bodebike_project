from django.shortcuts import render, get_object_or_404
from doencas.models import Doenca

def lista(request):
	pass
def detalhes(request,slug):
	context = {}

	doenca = get_object_or_404(Doenca, slug=slug)
	context['doenca'] = doenca

	vacina = Doenca.objects.get(nome= doenca.nome)
	context['tipoVacina'] = vacina
	

	return render(request, 'detalhesDoenca.html', context)
