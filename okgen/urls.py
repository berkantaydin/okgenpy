from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


admin.autodiscover()

#handler404 = 'errors.error404'
#handler500 = 'errors.error500'

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                       # okgen_cms
                       url(r'', include('okgen.okgen.okgen_banks.urls')),
                       # okgen_banks
                       url(r'', include('okgen.okgen.okgen_cms.urls')),


)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
else:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.STATIC_ROOT}),
    )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# flat pages
urlpatterns += patterns('django.contrib.flatpages.views',
                        (r'^(?P<url>.*/)$', 'flatpage'),
)