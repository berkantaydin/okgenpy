from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^links/bankalar/$', 'okgen_banks.views.banks', name='banks_banks'),
                       url(r'^banka/(?P<slug>[\w-]+)/$', 'okgen_banks.views.bank', name='banks_bank'),
                       url(r'^banka/subeler/(?P<slug>[\w-]+)/$', 'okgen_banks.views.branches', name='banks_branches'),
                       url(r'^banka/sube/(?P<id>[\w-]+)/$', 'okgen_banks.views.branch', name='banks_branch'),

)
