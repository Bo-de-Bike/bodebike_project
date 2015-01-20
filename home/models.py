# -*- coding: utf8 -*-
from django.db import models


class Vacina(models.Model):

	vacina = models.CharField('Nome da Vacina', max_length = 100)
	doenca = models.CharField('Doença', max_length = 100)
	dose = models.CharField('Dose', max_length = 100)
	dose_qtd = models.CharField('Dose_qtd', max_length = 100)
	via_administracao = models.CharField('Via Administração', max_length = 100)
	idade = models.CharField('Idade', max_length = 100)

	def __str__(self):
		return self.vacina

	class Meta:
		verbose_name = 'Vacina'
		verbose_name_plural = 'Vacinas'
		ordering = ['vacina']

class Doenca(models.Model):

	nome = models.CharField('Nome da Doença', max_length = 100)
	id_vacina = models.ForeignKey(Vacina, verbose_name='id_vacina', related_name='v_doenca')
	image = models.ImageField(upload_to= 'home/images', verbose_name='Imagem', null = True, blank = True )
	descricao = models.TextField('Sobre a Doença')
	slug = models.SlugField('Atalho')

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Doença'
		verbose_name_plural = 'Doenças'
		ordering = ['nome']


class Unidade_de_Vacinacao(models.Model):

	endereco = models.CharField('Endereço', max_length = 400)
	unidade = models.CharField('Unidade', max_length= 100)
	fone = models.IntegerField('Telefone', blank=True)
	latitude = models.IntegerField('latitude', blank=True)
	longitude = models.IntegerField('longitude', blank=True)

	def __str__(self):
		return self.unidade

	class Meta:
		verbose_name = 'Unidade de Vacinação'
		verbose_name_plural = 'Unidades de Vacinação'
		ordering = ['unidade']

