from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Chat
from .serializers import ChatSerializer
from openai import OpenAI
from decouple import config
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema


openai_api_key = config('GPT_KEY')
client = OpenAI(api_key=openai_api_key)


def ask_openai(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Вы полезный ассистент."},
            {"role": "user", "content": message},
        ],
    )

    answer = response.choices[0].message.content.strip()
    print(answer)
    return answer


class ChatBotAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ChatSerializer)
    def post(self, request):
        chats = Chat.objects.filter(user=request.user)

        message = request.data.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()

        serializer = ChatSerializer(chats, many=True)  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @swagger_auto_schema(request_body=ChatSerializer)
    def get(self, request):
        chats = Chat.objects.filter(user=request.user)
        serializer = ChatSerializer(chats, many=True)  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)