from django.db import models


class Vacina(models.Model):

	vacina = models.CharField('Nome da Vacina', max_length = 100)
	doenca = models.CharField('Doença', max_length = 100)
	dose = models.CharField('Dose', max_length = 100)
	dose_qtd = models.CharField('Dose_qtd', max_length = 100)
	via_administracao = models.CharField('Via Administração', max_length = 100)
	idade = models.CharField('Doença', max_length = 100)
	image = models.ImageField(upload_to= 'home/images', verbose_name='Imagem', null = True, blank = True )
	slug = models.SlugField('Atalho')
	sobre = models.TextField('Sobre a Vacina', blank = True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)


	def __str__(self):
		return self.vacina

	class Meta:
		verbose_name = 'Vacina'
		verbose_name_plural = 'Vacinas'
		ordering = ['vacina']
