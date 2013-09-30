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
                       (r'^$', include('okgen.okgen.okgen_cms.urls')),
                       url(r'link_clicked/(?P<id>\d+)/$', 'okgen_cms.views.link_clicked', name='cms_link_clicked'),
                       url(r'searched_words/(?P<page>\d+)/$', 'okgen_cms.views.searched_words',
                           name='cms_searched_words'),
                       url(r'^links/(?P<slug>[\w-]+)/$', 'okgen_cms.views.links', name='cms_links'),
                       # okgen_banks
                       url(r'bankalar/$', 'okgen_banks.views.banks', name='banks_banks'),
                       url(r'^banka/(?P<slug>[\w-]+)/$', 'okgen_banks.views.bank', name='banks_bank'),
                       url(r'^banka/subeler/(?P<slug>[\w-]+)/$', 'okgen_banks.views.branches', name='banks_branches'),
                       url(r'^banka/sube/(?P<slug>[\w-]+)/$', 'okgen_banks.views.branch', name='banks_branch'),

                       url(r'^sayfa$', include('django.contrib.flatpages.urls')),
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