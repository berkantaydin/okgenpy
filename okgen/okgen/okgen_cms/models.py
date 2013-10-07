from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.contrib.sitemaps import ping_google
from okgen.okgen.okgen_banks.models import Banks
from okgen.okgen.okgen_dreams.models import Dreams


class Words(models.Model):
    word = models.CharField(max_length=255)
    viewed = models.IntegerField(default=0)
    hidden = models.BooleanField(default=False)

    def get_absolute_url(self):
        return "/?searchid=2068377&text=%s&web=1" % self.word

    def save(self, force_insert=False, force_update=False):
        super(Words, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass


class Categories(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('name',))

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    def children_count(self):
        if self.slug == 'bankalar':
            return Banks.objects.count()
        if self.slug == 'ruya-tabirleri':
            return Dreams.objects.count()
        return Links.objects.filter(category=self).count()

    def children_five_random(self):
        if self.slug == 'ruya-tabirleri':
            return Dreams.objects.order_by('?').all()[:5]
        if self.slug == 'bankalar':
            return Banks.objects.order_by('?').all()[:5]
        return Links.objects.filter(category=self).order_by('?').all()[:5]

    def get_absolute_url(self):
        return reverse('cms_links', args={self.slug})

    def save(self, force_insert=False, force_update=False):
        super(Categories, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass


class Links(models.Model):
    text = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, null=True)
    link = models.CharField(max_length=255)
    clicked = models.IntegerField(default=1)
    hidden = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('cms_link_clicked', args={self.slug})

    def save(self, force_insert=False, force_update=False):
        super(Links, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass