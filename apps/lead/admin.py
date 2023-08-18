from django.contrib import admin

from .models import Lead


class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    list_filter = ('created',)
    search_fields = ('name', 'email', 'phone', 'message')
    date_hierarchy = 'created'
    ordering = ('created',)


admin.site.register(Lead, LeadAdmin)
