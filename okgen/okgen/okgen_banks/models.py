from django.db import models
from django_extensions.db.fields import AutoSlugField

class Banks(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('name',))
    callcenter = models.CharField(max_length=255)
    swift_code = models.CharField(max_length=20)
    eft_code = models.CharField(max_length=20)
    web_url = models.TextField(max_length=255)
    history = models.TextField(null=True)
    general_address = models.TextField(null=True)
    image = models.ImageField(upload_to='media')
    viewed = models.IntegerField(default=0)

    def get_branch_count(self):
        return 0