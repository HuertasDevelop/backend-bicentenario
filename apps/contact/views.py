from rest_framework import status, generics, permissions
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import ContactEnterprice


class ContactListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ContactSerializer
    queryset = ContactEnterprice.objects.first()

    def get(self, request, format=None):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
