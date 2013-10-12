from django.contrib.sitemaps import Sitemap
from .models import Banks


class BanksSitemap(Sitemap):
    priority = 0.5
    limit = 50000

    def items(self):
        return Banks.objects.all()
