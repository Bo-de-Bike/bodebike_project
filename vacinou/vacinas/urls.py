from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^$', 'vacinas.views.lista', name='lista'),
	url(r'^(?P<slug>[\w_-]+)/$', 'vacinas.views.detalhes', name='detalhes'),
)
