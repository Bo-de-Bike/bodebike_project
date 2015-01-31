from django.db import models

class Vacina(models.Model):
	name = models.CharField('Nome',max_length=100)
	age= models.IntegerField('Idade de uso')
	sickness = models.CharField('Doença', max_length=100)
	slug = models.SlugField('Atalho')
	start_date = models.DateField('Data de inicio',null=True,blank=True)
	description = models.TextField('Descriçao', blank=True)
	created_at= models.DateTimeField('Criado em', auto_now_add=True)
	updated_at=models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return ('vacinas:detalhes',(),{'slug':self.slug})

	class Meta:
		verbose_name = "Vacina"
		verbose_name_plural = "Vacina"
		ordering = ['name']

