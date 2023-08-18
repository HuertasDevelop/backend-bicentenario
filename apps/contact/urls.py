from django.urls import path
from .views import ContactListView
app_name = 'contact'
urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
]
