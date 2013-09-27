from django.db import models


class Words(models.Model):
    word = models.CharField(max_length=255)
    viewed = models.IntegerField(default=0)
    hidden = models.BooleanField(default=False)


class Links(models.Model):
    text = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    clicked = models.IntegerField(default=1)
    hidden = models.BooleanField(default=False)