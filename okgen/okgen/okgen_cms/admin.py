from django.contrib import admin
from okgen.okgen.okgen_cms.models import Words, Links


class WordsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Words, WordsAdmin)


class LinksAdmin(admin.ModelAdmin):
    pass
admin.site.register(Links, LinksAdmin)