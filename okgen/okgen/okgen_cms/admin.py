from django.contrib import admin
from okgen.okgen.okgen_cms.models import Words, Links


class WordsAdmin(admin.ModelAdmin):
    list_display = ('word', 'viewed', 'hidden')
    search_fields = ['word']
    pass
admin.site.register(Words, WordsAdmin)


class LinksAdmin(admin.ModelAdmin):
    list_display = ('text', 'link', 'clicked', 'hidden')
    pass
admin.site.register(Links, LinksAdmin)