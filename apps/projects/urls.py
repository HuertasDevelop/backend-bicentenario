from django.urls import path
from .views import ProjectListView, ProjectSlugView
app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('<slug>/', ProjectSlugView.as_view()),

]
