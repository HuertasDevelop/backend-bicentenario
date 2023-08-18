from rest_framework import status, generics, permissions
from rest_framework.response import Response

from .models import About, Office, Stats
from .serializers import AboutSerializer, OfficeSerializer, StatsSerializer


class AboutListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = AboutSerializer
    queryset = About.objects.all()

    def get(self, request, format=None):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class OfficeListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = OfficeSerializer
    queryset = Office.objects.all()

    def get(self, request, format=None):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class StatsListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = StatsSerializer
    queryset = Stats.objects.all()

    def get(self, request, format=None):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
