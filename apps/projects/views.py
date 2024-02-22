from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorPermission, IsAdminPermission

# Create your views here.


class PermissionMixin:
    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]


class ProjectViewSet(PermissionMixin, ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]