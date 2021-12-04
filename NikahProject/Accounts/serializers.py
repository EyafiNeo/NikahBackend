from django.db.models import fields
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer

from Accounts.models import UserProfile, profileInfo


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "name",
            "email",
            "username",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            name = validated_data["name"],
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )

        return user
    

class profileInfoSerializer(ModelSerializer):
    class Meta:
        model = profileInfo
        fields = "__all__"
