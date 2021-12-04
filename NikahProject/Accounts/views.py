from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from Accounts.models import UserProfile,profileInfo
from Accounts.serializers import UserProfileSerializer, profileInfoSerializer

# Create your views here.
class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class profileInfoViewset(ModelViewSet):
    serializer_class = profileInfoSerializer
    queryset = profileInfo.objects.all()