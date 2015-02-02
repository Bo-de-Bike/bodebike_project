# -*- coding: utf8 -*-
from django.db import models

class Unidade_de_Vacinacao(models.Model):

	endereco = models.CharField('Endereço', max_length = 400)
	unidade = models.CharField('Unidade', max_length= 100)
	bairro = models.CharField('Bairro', max_length = 30)
	fone = models.CharField('Telefone', blank=True, max_length=14)
	latitude = models.CharField('latitude', blank=True, max_length=20)
	longitude = models.CharField('longitude', blank=True,max_length=20)
	slug = models.SlugField('Atalho')

	def __str__(self):
		return self.unidade

	class Meta:
		verbose_name = 'Unidade de Vacinação'
		verbose_name_plural = 'Unidades de Vacinação'
		ordering = ['unidade']

