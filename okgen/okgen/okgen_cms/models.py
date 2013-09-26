from django.db import models


class Words(models.Model):
    word = models.CharField(max_length=255)
    viewed = models.IntegerField(default=0)
    hidden = models.BooleanField(default=False)