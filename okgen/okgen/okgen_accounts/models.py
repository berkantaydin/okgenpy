import random
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='user')
    is_deleted = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    key_activation = models.CharField(max_length=12, default=str(random.random())[2:14])
    slug = AutoSlugField(_('slug'), max_length=50, unique=True, populate_from=('user',))

    def email(self):
        return self.user.email

    def __unicode__(self):
        return '%s' % self.user.username
