from django.contrib import admin
from okgen.okgen.okgen_cms.models import Words, Links, Categories
from mptt.admin import MPTTModelAdmin


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    pass


admin.site.register(Categories, CustomMPTTModelAdmin)


class WordsAdmin(admin.ModelAdmin):
    list_display = ('word', 'viewed', 'hidden')
    search_fields = ['word']
    pass


admin.site.register(Words, WordsAdmin)


class LinksAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'tags__name', 'link', 'clicked', 'hidden')
    pass


admin.site.register(Links, LinksAdmin)