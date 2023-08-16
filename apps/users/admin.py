from django.contrib.auth.models import Group
from social_django.models import Association, Nonce, UserSocialAuth
from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()


admin.site.site_header = 'Web Bicentenario admin - Belmont'
admin.site.site_title = 'Web Bicentenario admin '
admin.site.index_title = 'Sitio administrativo Web Bicentenario'
admin.site.site_url = 'https://www.webbicentenario.com/'


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff',
                    'is_superuser', 'is_active',  'last_login')
    list_display_links = ('email', )
    search_fields = ('email', 'username'
                     )
    list_filter = ('is_superuser', 'is_active',)

    list_per_page = 25
    exclude = ('last_login',
               'groups', 'user_permissions')


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)
