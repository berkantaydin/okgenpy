from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()

#handler404 = 'errors.error404'
#handler500 = 'errors.error500'

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),

                       # okgen_cms
                       (r'^$', include('okgen.okgen.okgen_cms.urls')),
                       url(r'link_clicked/(?P<id>\d+)/$', 'okgen_cms.views.link_clicked', name='cms_link_clicked'),
                       url(r'speed_test/$', 'okgen_cms.views.speed_test', name='cms_speed_test'),

                       # okgen_banks
                       # url(r'bankalar/$', 'okgen_banks.views.banks', name='banks_banks'),
                       # url(r'banka/(?P<id>\d+)/$', 'okgen_banks.views.bank', name='banks_bank'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()