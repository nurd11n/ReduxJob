from rest_framework.serializers import ModelSerializer, ReadOnlyField, SerializerMethodField
from .models import ChatRoom, Message

class MessageSerializer(ModelSerializer):
    sender = ReadOnlyField(source='sender.email')

    class Meta:
        model = Message
        fields = ('id', 'chatroom', 'sender', 'text', 'timestamp')

    def create(self, validated_data):
        user = self.context['request'].user
        project = Message.objects.create(sender=user, **validated_data)
        return project


class ChatRoomSerializer(ModelSerializer):
    admin = ReadOnlyField(source='admin.email')
    created_by = ReadOnlyField(source='created_by.email')

    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        fields = ('id', 'admin', 'title', 'participants', 'created_at', 'created_by', 'messages')


    def create(self, validated_data):
        user = self.context['request'].user
        participants_data = validated_data.pop('participants', [])
        chatroom = ChatRoom.objects.create(created_by=user, admin=user, **validated_data)
        chatroom.participants.set(participants_data)
        return chatroom

