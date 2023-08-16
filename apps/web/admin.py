from django.contrib import admin

from .models import Carousel, HomePage, Comment, ProjectPage


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('link', 'photo', 'active', 'order')
    list_filter = ('active',)
    list_editable = ('active', 'order')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'active')
    list_filter = ('active',)
    search_fields = ('name',)
    list_editable = ('active',)


class HomePageAdmin(admin.ModelAdmin):
    list_display = ('link', 'photo', 'type')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ProjectPageAdmin(admin.ModelAdmin):
    list_display = ('link', 'photo', 'type')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Carousel, CarouselAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ProjectPage, ProjectPageAdmin)
