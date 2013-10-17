from django.contrib import admin
from okgen.okgen.okgen_banks.models import Banks, City, Town, County, Branches


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ['name']
    pass


admin.site.register(City, CityAdmin)


class TownAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'city')
    search_fields = ['name']
    pass


admin.site.register(Town, TownAdmin)


class CountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'city')
    search_fields = ['name']
    pass


admin.site.register(County, CountyAdmin)


class BanksAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'viewed')
    search_fields = ['name']
    pass


admin.site.register(Banks, BanksAdmin)


class BranchesAdmin(admin.ModelAdmin):
    list_display = ('name', 'town',)
    search_fields = ['name']
    pass


admin.site.register(Branches, BranchesAdmin)
