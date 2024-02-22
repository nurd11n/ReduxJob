from rest_framework.viewsets import ModelViewSet
from .models import UserProfile, CompanyProfile
from .serializer import UserPSerializer, CompanyPSerializer
from .permissions import IsAuthorPermission, IsAdminPermission
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# Create your views here.


class UserPViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserPSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [AllowAny]
        else:
            permissions = [IsAuthorPermission, IsAdminPermission]
        return [permission() for permission in permissions]


class CompanyPViewSet(ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyPSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [AllowAny]
        else:
            permissions = [IsAuthorPermission, IsAdminPermission]
        return [permission() for permission in permissions]
