from .views import AboutListView, OfficeListView, StatsListView
from django.urls import path

app_name = 'about'

urlpatterns = [
    path('', AboutListView.as_view()),
    path('office/', OfficeListView.as_view()),
    path('stats/', StatsListView.as_view()),
]
