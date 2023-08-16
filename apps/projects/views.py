from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.shortcuts import get_object_or_404

from .serializers import ProjectSerializer
from .models import Project


class ProjectListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self, request, format=None):
        try:

            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProjectSlugView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self, request, slug, format=None):
        project = get_object_or_404(self.get_queryset(), slug=slug)

        serializer = self.serializer_class(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
