# -*- coding: utf8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^(?P<slug>[\w_-]+)/$', 'doencas.views.detalhes', name='detalhes'),
)
