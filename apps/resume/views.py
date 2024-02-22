from rest_framework.views import APIView
from rest_framework.viewsets import generics, ModelViewSet
from .serializers import ResumeSerializer, OtherResumeSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAuthorPermission, IsAdminPermission
from .models import Resume, OtherResume
from drf_yasg.utils import swagger_auto_schema
from rest_framework.serializers import ValidationError


User = get_user_model()


class ResumeView(APIView):
    permission_classes = [IsAuthenticated, IsAuthorPermission]

    def validate_specialization(self, specialization):
        user = self.request.user
        existing_resume = Resume.objects.filter(user=user, specialization=specialization).first()
        if existing_resume:
            raise ValidationError('Вы уже создали резюме с такой специализацией')

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            specialization = serializer.validated_data.get('specialization')
            self.validate_specialization(specialization)
            serializer.save(user=self.request.user)
        else:
            raise ValidationError('Пользователь не аутентифицирован')

    @swagger_auto_schema(request_body=ResumeSerializer())
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response('Ваше резюме успешно размещено на сайте! Проверьте почту')

    def get(self, request):
        users_resume = Resume.objects.filter(user=request.user)
        serializer = ResumeSerializer(users_resume, many=True)
        return Response(serializer.data)


class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, IsAdminPermission]


# class EmployerResumeRetrieveView(generics.RetrieveAPIView):
#     permission_classes = [IsAuthenticated, IsEmployer]
#     queryset = Resume.objects.all()
#     serializer_class = EmployerResumeSerializer
#     lookup_field = 'slug'

    # def get_queryset(self):
    #     return Vacancy.objects.filter(applicants=self.request.user)


class OtherResumeViewSet(ModelViewSet):
    queryset = OtherResume.objects.all()
    serializer_class = OtherResumeSerializer
    permission_classes = IsAuthorPermission

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission, IsAdminPermission]
        return [permission() for permission in permissions]
