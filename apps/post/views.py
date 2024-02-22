from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Post, ErCode, Forum, CompanyPost, CompanyVacancy, DitailCompanyPost, DitailCompanyVacancy, DitailUserPost
from .serializers import (PostSerializer, ForumSerializer, ErCodeSerializer, CompanyVacancySerializer,
                          CompanyPostSerializer, DitailCompanyVacancySerializer,
                          DitailCompanyPostSerializer, DitailUserPostSerializer, ListCompanyPostSerializer,
                          ListForumSerializer, ListErCodeSerializer, ListPostSerializer, ListCompanyVacancySerializer)
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .permissions import IsAuthorPermission, IsAdminPermission
from apps.review.models import Like
from apps.review.serializers import CommentActionSerializer, LikeSerializer
from rest_framework.decorators import action
from rest_framework import filters
import django_filters

# Create your views here.


# class PermissionMixin:
#     def get_permissions(self):
#         if self.action in ('list', 'retrieve'):
#             permissions = [IsAuthenticated]
#         elif self.action == 'create':
#             permissions = [IsAuthenticated]
#         else:
#             permissions = [IsAuthorPermission]
#         return [permission() for permission in permissions]

class PermissionMixin:
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy', 'create'):
            permissions = [IsAdminUser]
        else:
            permissions = [AllowAny]
        return [permissions() for permissions in permissions]


class PostViewSet(PermissionMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'type_post', 'celery']
    search_fields = ['name', 'type_post', 'celery']
    ordering_fields = ['type_post', 'name']

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return ListPostSerializer
        return self.serializer_class


class ErCodeViewSet(PermissionMixin, ModelViewSet):
    queryset = ErCode.objects.all()
    serializer_class = ErCodeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return ListErCodeSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]


class ForumViewSet(ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return ListForumSerializer
        return self.serializer_class

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        forum = self.get_object()
        user = request.user
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = Like.objects.get(forum=forum, author=user)
                like.delete()
                message = 'Unlike'
            except Like.DoesNotExist:
                Like.objects.create(forum=forum, author=user)
                message = 'Like'
            return Response(message, status=200)

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def comments(self, request, pk=None):
        video = self.get_object()
        user = request.user
        serializer = CommentActionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(video=video, author=user)
            message = request.data
            return Response(message, status=200)


    # def get_permissions(self):
    #     if self.action in ('list', 'retrieve'):
    #         permissions = [IsAuthenticated]
    #     elif self.action == 'create':
    #         permissions = [IsAuthenticated]
    #     else:
    #         permissions = [IsAuthorPermission]
    #     return [permission() for permission in permissions]


    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class CompanyPostViewSet(PermissionMixin, ModelViewSet):
    queryset = CompanyPost.objects.all()
    serializer_class = CompanyPostSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'type_post', 'celery']
    search_fields = ['name', 'type_post', 'celery']
    ordering_fields = ['type_post', 'name']

    def get_serializer_class(self):
        if self.action == 'list':
            return ListCompanyPostSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class CompanyVacancyViewSet(PermissionMixin, ModelViewSet):
    queryset = CompanyVacancy.objects.all()
    serializer_class = CompanyVacancySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'type_work', 'celery', 'type_employment']
    search_fields = ['title', 'type_work', 'type_employment', 'celery']
    ordering_fields = ['type_work', 'title']

    def get_serializer_class(self):
        if self.action == 'list':
            return ListCompanyVacancySerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]


class DitailCompanyPostViewSet(PermissionMixin, ModelViewSet):
    queryset = DitailCompanyPost.objects.all()
    serializer_class = DitailCompanyPostSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]


class DitailCompanyVacancyViewSet(PermissionMixin, ModelViewSet):
    queryset = DitailCompanyVacancy.objects.all()
    serializer_class = DitailCompanyVacancySerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]


class DitailUserPostViewSet(PermissionMixin, ModelViewSet):
    queryset = DitailUserPost.objects.all()
    serializer_class = DitailUserPostSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]