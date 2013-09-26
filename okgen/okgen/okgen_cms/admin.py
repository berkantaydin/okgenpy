from django.contrib import admin
from okgen_cms.models import Words


class WordsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Words, WordsAdmin)