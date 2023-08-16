from django.contrib import admin
from .models import Areas, Benefits,  Project, Gallery


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'type_coin', 'from_price', 'price',
                    'from_area')
    list_filter = ('place', 'name', )
    search_fields = ('name', 'place', )
    list_per_page = 10
    inlines = [GalleryInline]


class AreasAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', )
    list_filter = ('name',)
    search_fields = ('name', )
    list_per_page = 16


class BenefitsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 10


admin.site.register(Areas, AreasAdmin)
admin.site.register(Benefits, BenefitsAdmin)
admin.site.register(Project, ProjectAdmin)
