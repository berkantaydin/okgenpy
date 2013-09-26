from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()

#handler404 = 'errors.error404'
#handler500 = 'errors.error500'

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                       url(r'^$', include('okgen_cms.urls')),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()