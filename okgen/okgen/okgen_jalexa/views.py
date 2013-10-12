from urlparse import urlparse
from django.shortcuts import HttpResponse
from .models import Sites


def js(request):
    # TODO: get url from GET['url'] and add point
    try:
        site = Sites()
        site = site.get_random_one()
    except:
        site = "okgen.com"

    return HttpResponse(
        """
        (function() {
            var s = document.createElement('script');
            s.type = 'text/javascript';
            s.async = true;
            s.src = 'http://xslt.alexa.com/site_stats/js/t/a?url=%s';
            var x = document.getElementsByTagName('script')[0];
            x.parentNode.insertBefore(s, x);
        })();
        """ % site)