from rest_framework import serializers
from .models import Chat


class ChatSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Chat
        fields = '__all__'
