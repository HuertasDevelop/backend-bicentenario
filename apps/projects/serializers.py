
from .models import Areas, Project, Benefits, Gallery
from rest_framework import serializers


class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = ('id', 'name', 'photo', )


class BenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
        fields = ('id', 'name', 'description', )


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'name', 'alt', )


class ProjectSerializer(serializers.ModelSerializer):
    areas = AreasSerializer(many=True, read_only=True)
    benefits = BenefitsSerializer(many=True, read_only=True)
    gallery = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'place',
            'from_area',
            'type_coin',
            'people_card',
            'banner_card',
            'slogan',
            'banner_detail',
            'banner',
            'link_banner_video',
            'location',
            'ref_location',
            'areas',
            'photo_map',
            'link_google_maps',
            'link_waze',
            'photo_feature',
            'benefits',
            'gallery',
        )
