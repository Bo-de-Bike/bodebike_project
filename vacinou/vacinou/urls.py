from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('core.urls', namespace = 'core')),
    url(r'^vacinas/', include('vacinas.urls', namespace = 'vacinas')),
    url(r'^doencas/', include('doencas.urls', namespace = 'doencas')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)