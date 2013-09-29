from django.db import models
from django_extensions.db.fields import AutoSlugField


class City(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('name',))

    def __unicode__(self):
        return '%s' % self.name


class Town(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('name',))
    city = models.ForeignKey(City)

    def __unicode__(self):
        return '%s' % self.name


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

    def get_branch_count(self):
        return 0


class Branches(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('name',))
    city = models.ForeignKey(City)
    town = models.ForeignKey(Town)
    phone = models.CharField(max_length=255)
    address = models.TextField(null=True)
    viewed = models.IntegerField(default=0)