from .views import AboutListView, OfficeListView, StatsListView
from django.urls import path

urlpatterns = [
    path('', AboutListView.as_view(), name='about'),
    path('office/', OfficeListView.as_view(), name='office'),
    path('stats/', StatsListView.as_view(), name='stats'),
]
