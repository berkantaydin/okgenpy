from django.db import models
from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.contrib.sitemaps import ping_google


class City(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('name',))

    class Meta:
        ordering = ['name', ]

    def __unicode__(self):
        return '%s' % self.name


class Town(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('name',))
    city = models.ForeignKey(City)

    class Meta:
        ordering = ['city__name', 'name', ]

    def __unicode__(self):
        return '%s > %s' % (self.city, self.name)


class County(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('name',))
    city = models.ForeignKey(City)
    town = models.ForeignKey(Town)

    class Meta:
        ordering = ['city__name', 'town__name', 'name', ]

    def __unicode__(self):
        return '%s > %s > %s' % (self.city, self.town, self.name)


class Banks(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('name',))
    call_center = models.CharField(max_length=255)
    swift_code = models.CharField(max_length=20)
    eft_code = models.CharField(max_length=20)
    web_url = models.CharField(max_length=255)
    history = models.TextField(null=True)
    general_address = models.TextField(null=True)
    city = models.ForeignKey(City)
    town = models.ForeignKey(Town)
    image = models.ImageField(upload_to='media')
    viewed = models.IntegerField(default=0)

    class Meta:
        ordering = ['name', ]

    def __unicode__(self):
        return self.name

    def get_branch_count(self):
        return 0

    def get_absolute_url(self):
        return reverse('banks_bank', args={self.slug})

    def save(self, force_insert=False, force_update=False):
        super(Banks, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass


class Branches(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('name',))
    bank = models.ForeignKey(Banks)
    city = models.ForeignKey(City)
    town = models.ForeignKey(Town)
    branch_code = models.CharField(max_length=20)
    swift_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    opentime = models.TextField(null=True)
    address = models.TextField(null=True)
    viewed = models.IntegerField(default=0)

    class Meta:
        ordering = ['bank__name', 'name', ]