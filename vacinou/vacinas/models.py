from django.db import models

class Vacina(models.Model):
	idade= models.CharField('Idade de uso', max_length=15)
	nome = models.CharField('Nome',max_length=100)
	doenca_protecao = models.CharField('Trata doença', max_length=200)
	dose = models.CharField('Dose', max_length=200)
	dose_qtd = models.CharField('Quantidade da dose', max_length=50, null=True,blank=True)
	via_administracao = models.CharField('Via de aplicaçao', max_length=25, null=True,blank=True)
	descricao = models.TextField('Descriçao', blank=True)
	slug = models.SlugField('Atalho')
	image = models.ImageField(upload_to= 'home/images', verbose_name='Imagem', null = True, blank = True )

	def __str__(self):
		return self.nome

	@models.permalink
	def get_absolute_url(self):
		return ('vacinas:detalhes',(),{'slug':self.slug})

	class Meta:
		verbose_name = "Vacina"
		verbose_name_plural = "Vacina"
		ordering = ['nome']

