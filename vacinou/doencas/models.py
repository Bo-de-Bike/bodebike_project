# -*- coding: utf8 -*-
from django.db import models
from vacinas.models import Vacina

class Doenca(models.Model):

	nome = models.CharField('Nome da Doença', max_length = 100)
	id_vacina = models.ManyToManyField(Vacina, verbose_name='id_vacina', related_name='v_doenca')
	image = models.ImageField(upload_to= 'home/images', verbose_name='Imagem', null = True, blank = True )
	descricao = models.TextField('Sobre a Doença')
	slug = models.SlugField('Atalho')

	def __str__(self):
		return self.nome

	@models.permalink
	def get_absolute_url(self):
		return ('doencas:detalhes',(), {'slug':self.slug})

	class Meta:
		verbose_name = 'Doença'
		verbose_name_plural = 'Doenças'
		ordering = ['nome']

