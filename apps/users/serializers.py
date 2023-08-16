from rest_framework.serializers import ModelSerializer

from .models import UserAccount


class CustomUserModelSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_configured',
        ]

    def create(self, validated_data):

        user = UserAccount.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )

        return user
