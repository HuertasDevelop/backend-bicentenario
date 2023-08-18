
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/', include('djoser.urls')),
    path('api/', include('apps.users.urls')),
    path('api/projects/', include('apps.projects.urls')),
    path('api/web/', include('apps.web.urls')),
    path('api/contact/', include('apps.contact.urls')),
    path('api/about/', include('apps.about.urls')),


    path('', admin.site.urls),
]
