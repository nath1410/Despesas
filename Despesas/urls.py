from django.conf.urls import patterns, include, url
#from django.contrib.staticfiles.url import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'dashboard.views.index', name='Despesas_index'),
    url(r'^config/', 'Inicio.views.config', name='Despesas_config'),
    url(r'^conta/', 'Inicio.views.conta', name='Despesas_conta'),
    url(r'^ajuda/', 'Inicio.views.ajuda', name='Despesas_ajuda'),
    url(r'^admin/', include(admin.site.urls)),
)
