from .models import About, Office, Stats
from rest_framework import serializers


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'
