from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
from .models import Like, Comment


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment


class CommentActionSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    video = ReadOnlyField()

    class Meta:
        model = Comment
        fields = '__all__'

    def validate_product(self, video):
        user = self.context.get('request').user
        if self.Meta.model.objects.filter(video=video, author=user):
            raise ValidationError(
                "You can't be rating"
            )
        return video

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        return comment


class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    forum = ReadOnlyField()

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        return self.Meta.model.objects.create(author=user, **validated_data)


class LikeSeeSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Like.objects.create(author=user, **validated_data)
        return comment
