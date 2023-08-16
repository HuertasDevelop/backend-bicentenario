from rest_framework import serializers
from .models import Carousel, HomePage, Comment, ProjectPage


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ('id', 'description', 'link', 'photo', 'active', 'order', )


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = ('id', 'description', 'link', 'photo', 'type', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'comment', 'photo')


class ProjectPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPage
        fields = ('id', 'description', 'link', 'photo', 'type', )
