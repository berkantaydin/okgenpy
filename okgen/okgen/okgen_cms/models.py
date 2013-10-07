from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django_extensions.db.fields import AutoSlugField
from okgen.okgen.okgen_banks.models import Banks
from okgen.okgen.okgen_dreams.models import Dreams


class Words(models.Model):
    word = models.CharField(max_length=255)
    viewed = models.IntegerField(default=0)
    hidden = models.BooleanField(default=False)


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



class Links(models.Model):
    text = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, null=True)
    link = models.CharField(max_length=255)
    clicked = models.IntegerField(default=1)
    hidden = models.BooleanField(default=False)