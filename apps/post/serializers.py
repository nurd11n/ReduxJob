from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Post, Forum, ErCode, CompanyVacancy, CompanyPost, DitailCompanyVacancy, DitailCompanyPost, DitailUserPost
from django.contrib.auth import get_user_model
from apps.review.serializers import CommentSerializer

User = get_user_model()


class ListPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'name', 'type_post', 'description', 'celery']


class PostSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField(source='profile.id')

    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['desc'] = DitailUserPostSerializer(instance.ditail_user_post.all(), many=True).data
        return rep

    def create(self, validated_data):
        user = self.context['request'].user
        profile = user.user_profile
        post = Post.objects.create(user=user, profile=profile, **validated_data)
        return post


class PostViewSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class ListForumSerializer(ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'name']


class ForumSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField(source='profile.id')

    class Meta:
        model = Forum
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        rep['like'] = instance.likes.all().count()
        return rep

    def create(self, validated_data):
        user = self.context['request'].user
        profile = user.user_profile
        forum = Forum.objects.create(user=user, profile=profile, **validated_data)
        return forum


class ForumViewSerializer(ModelSerializer):
    class Meta:
        model = Forum
        fields = "__all__"


class ListErCodeSerializer(ModelSerializer):
    class Meta:
        model = ErCode
        fields = ['id', 'name']


class ErCodeSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField(source='profile.id')

    class Meta:
        model = ErCode
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        profile = user.user_profile
        ercode = ErCode.objects.create(user=user, profile=profile, **validated_data)
        return ercode


class ErCodeViewSerializer(ModelSerializer):
    class Meta:
        model = ErCode
        fields = "__all__"


class ListCompanyPostSerializer(ModelSerializer):
    class Meta:
        model = CompanyPost
        fields = ['id', 'name', 'type_post', 'description', 'celery']


class CompanyPostSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField(source='profile.id')

    class Meta:
        model = CompanyPost
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['desc'] = DitailCompanyPostSerializer(instance.ditail_company_post.all(), many=True).data
        return rep

    def create(self, validated_data):
        user = self.context['request'].user
        profile = user.company_profile
        comppost = CompanyPost.objects.create(user=user, profile=profile, **validated_data)
        return comppost


class CompanyPostSerializerView(ModelSerializer):
    class Meta:
        model = CompanyPost
        fields = "__all__"


class ListCompanyVacancySerializer(ModelSerializer):
    class Meta:
        model = CompanyVacancy
        fields = ['id', 'title', 'position', 'type_employment', 'type_work']


class CompanyVacancySerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField(source='profile.id')

    class Meta:
        model = CompanyVacancy
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['desc'] = DitailCompanyVacancySerializer(instance.ditail_company_vacancy.all(), many=True).data
        return rep

    def create(self, validated_data):
        user = self.context['request'].user
        profile = user.company_profile
        compvac = CompanyVacancy.objects.create(user=user, profile=profile, **validated_data)
        return compvac


class CompanyVacancySerializerView(ModelSerializer):
    class Meta:
        model = CompanyVacancy
        fields = "__all__"


class DitailCompanyVacancySerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    class Meta:
        model = DitailCompanyVacancy
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        ditail_comp_vac = DitailCompanyVacancy.objects.create(user=user, **validated_data)
        return ditail_comp_vac


class DitailCompanyPostSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')

    class Meta:
        model = DitailCompanyPost
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        ditail_comp_post = DitailCompanyPost.objects.create(user=user, **validated_data)
        return ditail_comp_post


class DitailUserPostSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')

    class Meta:
        model = DitailUserPost
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        ditail_user_post = DitailUserPost.objects.create(user=user, **validated_data)
        return ditail_user_post
