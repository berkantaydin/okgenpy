from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps.views import index as sitemap_index, sitemap
from okgen.okgen_banks.sitemap import BanksSitemap
from okgen.okgen_dreams.sitemap import DreamsSitemap
from okgen.okgen_cms.sitemap import CategoriesSitemap, LinksSitemap, WordsSitemap

admin.autodiscover()

#handler404 = 'errors.error404'
#handler500 = 'errors.error500'

sitemaps = {
    "banks": BanksSitemap,
    "dreams": DreamsSitemap,
    "linkcats": CategoriesSitemap,
    "links": LinksSitemap,
    #"words": WordsSitemap,
}

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),

                       # sitemaps
                       url(r'^sitemap\.xml$', sitemap_index,
                           {'sitemaps': sitemaps, 'template_name': 'sitemap-index.html'}),

                       (r'^sitemap-(?P<section>.+)\.xml', sitemap,
                        {'sitemaps': sitemaps, 'template_name': 'sitemap.html'}),

                       # photo gallery
                       (r'^photologue/', include('photologue.urls')),

                       # okgen_banks
                       url(r'', include('okgen.okgen.okgen_banks.urls')),
                       # okgen_dreams
                       url(r'', include('okgen.okgen.okgen_dreams.urls')),
                       # okgen_cms
                       url(r'', include('okgen.okgen.okgen_cms.urls')),


)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
else:
    urlpatterns += patterns('',
                            (r'^staticus/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.STATIC_ROOT}),
    )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# flat pages
urlpatterns += patterns('django.contrib.flatpages.views',
                        (r'^(?P<url>.*/)$', 'flatpage'),
)