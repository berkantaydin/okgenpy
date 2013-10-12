from django.contrib.sitemaps import Sitemap
from .models import Dreams


class DreamsSitemap(Sitemap):
    priority = 0.5
    limit = 50000

    def items(self):
        return Dreams.objects.all()
