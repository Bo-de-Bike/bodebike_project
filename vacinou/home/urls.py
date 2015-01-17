from django.conf.urls import patterns, include, url
from home.views import home

urlpatterns = patterns('',

	url(r'^$', home.as_view(), name='home'),
)
