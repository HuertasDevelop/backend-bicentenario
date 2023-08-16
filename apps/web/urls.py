from django.urls import path
from .views import CarouselListView, HomePageListView, CommentListView, ProjectPageListView
app_name = 'web'


urlpatterns = [
    path('carousel/', CarouselListView.as_view(), name='carousel_list'),
    path('home/', HomePageListView.as_view(), name='home_list'),
    path('comment/', CommentListView.as_view(), name='comment_list'),
    path('project/', ProjectPageListView.as_view(), name='project_list'),
]
