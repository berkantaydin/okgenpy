from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^jalexa/js/$', 'okgen_jalexa.views.js', name='jalexa_js'),
)
