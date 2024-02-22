from rest_framework.serializers import ModelSerializer
from .models import CompanyProfile, UserProfile
from apps.resume.serializers import OtherResumeSeeSerializer, ResumeSerializer
from apps.projects.serializers import ProjectViewSerializer
from apps.post.serializers import ErCodeViewSerializer, PostViewSerializer, ForumViewSerializer, CompanyPostSerializer, CompanyVacancySerializer


class UserPSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['post'] = PostViewSerializer(instance.posts.all(), many=True).data
        rep['forum'] = ForumViewSerializer(instance.forum.all(), many=True).data
        rep['er_code'] = ErCodeViewSerializer(instance.ercode.all(), many=True).data
        rep['project'] = ProjectViewSerializer(instance.projects.all(), many=True).data
        rep['resume1'] = ResumeSerializer(instance.resume.all(), many=True).data
        rep['upload_resume'] = OtherResumeSeeSerializer(instance.other_resume.all(), many=True).data
        return rep


class CompanyPSerializer(ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = "__all__"


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['post'] = CompanyPostSerializer(instance.company_posts.all(), many=True).data
        rep['vacancy'] = CompanyVacancySerializer(instance.company_vacancy.all(), many=True).data
        return rep
