from django.contrib import admin
from okgen.okgen.okgen_dreams.models import Dreams


class DreamsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    pass


admin.site.register(Dreams, DreamsAdmin)