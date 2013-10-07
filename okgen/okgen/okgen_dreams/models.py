from django.db import models
from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.contrib.sitemaps import ping_google


class Dreams(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('name',))
    text = models.TextField()

    class Meta:
        ordering = ['name', ]

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dreams_dream', args={self.slug})

    def save(self, force_insert=False, force_update=False):
        super(Dreams, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass