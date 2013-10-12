from django.db import models


class Sites(models.Model):
    url = models.CharField(max_length=255)
    credits = models.BigIntegerField(default=1)

    class Meta:
        ordering = ['url', ]

    def __unicode__(self):
        return self.url

    def get_random_one(self):
        return Sites.objects.filter(credits__gte=0).order_by('?').all()[0]
