from .models import ContactEnterprice
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEnterprice
        fields = '__all__'
