from django.db import models
from django_extensions.db.fields import AutoSlugField


class Dreams(models.Model):
    name = models.CharField(max_length=255)
    #slug = AutoSlugField(max_length=50, unique=True, populate_from=('name',))
    text = models.TextField()

    class Meta:
        ordering = ['name', ]

    def __unicode__(self):
        return self.name