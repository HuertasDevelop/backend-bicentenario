from django.contrib import admin
from .models import ContactEnterprice


class ContactAdmin(admin.ModelAdmin):
    list_display = ('banner_top', 'banner_bot',
                    'people_photo', 'photo_number_phone',)


admin.site.register(ContactEnterprice, ContactAdmin)
