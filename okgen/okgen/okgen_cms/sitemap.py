from django.contrib.sitemaps import Sitemap
from .models import Categories, Links, Words


class CategoriesSitemap(Sitemap):
    priority = 0.5
    limit = 50000

    def items(self):
        return Categories.objects.all()


class LinksSitemap(Sitemap):
    priority = 0.5
    limit = 50000

    def items(self):
        return Links.objects.all()


class WordsSitemap(Sitemap):
    priority = 0.5
    limit = 50000

    def items(self):
        return Words.objects.all()
