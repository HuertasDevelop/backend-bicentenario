from django.contrib import admin

from .models import About, Stats, Office


class AboutAdmin(admin.ModelAdmin):
    list_display = ('description', 'banner_bg', 'banner_info')


class StatsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class OfficeAdmin(admin.ModelAdmin):
    list_display = ('address', 'reference', 'link_google_maps', 'link_waze')


admin.site.register(About, AboutAdmin)
admin.site.register(Stats, StatsAdmin)
admin.site.register(Office, OfficeAdmin)
