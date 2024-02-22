from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Project
from django.contrib.auth import get_user_model


User = get_user_model()


class ProjectSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField(source='profile.id')

    class Meta:
        model = Project
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        profiles = user.user_profile
        project = Project.objects.create(user=user, profile=profiles, **validated_data)
        return project


class ProjectViewSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
