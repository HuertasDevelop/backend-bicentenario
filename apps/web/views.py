from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .serializers import CarouselSerializer, HomePageSerializer, CommentSerializer, ProjectPageSerializer
from .models import Carousel, HomePage, Comment, ProjectPage


class CarouselListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = CarouselSerializer
    queryset = Carousel.objects.all()

    def get(self, request, format=None):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class HomePageListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = HomePageSerializer
    queryset = HomePage.objects.all()

    def get(self, request, format=None):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProjectPageListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProjectPageSerializer
    queryset = ProjectPage.objects.all()

    def get(self, request, format=None):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(active=True)

    def get(self, request, format=None):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
