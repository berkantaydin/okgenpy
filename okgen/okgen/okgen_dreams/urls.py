from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^links/ruya-tabirleri/$', 'okgen_dreams.views.dreams', name='dreams_dreams'),
                       url(r'^ruya-tabiri/(?P<slug>[\w-]+)/$', 'okgen_dreams.views.dream', name='dreams_dream'),
)
