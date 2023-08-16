from django.urls import path
from .views import ProjectListView, ProjectSlugView
app_name = 'projects'
# admin site name

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<slug>/', ProjectSlugView.as_view()),

]
