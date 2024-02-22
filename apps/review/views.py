from .models import Like, Comment
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from .perimissions import IsAuthor
from drf_yasg.utils import swagger_auto_schema


# Create your views here.

class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated]
        elif self.action in ('update', 'partial_update', 'destroy'):
            permissions = [IsAuthor]
        else:
            permissions = [AllowAny]
        return [permissions() for permissions in permissions]


class CommentView(PermissionMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeView(PermissionMixin, ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSeeSerializer
