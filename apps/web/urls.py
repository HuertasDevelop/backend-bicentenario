from django.urls import path
from .views import CarouselListView, HomePageListView, CommentListView, ProjectPageListView
app_name = 'web'

urlpatterns = [
    path('carousel/', CarouselListView.as_view()),
    path('home/', HomePageListView.as_view()),
    path('comment/', CommentListView.as_view()),
    path('project/', ProjectPageListView.as_view()),
]
