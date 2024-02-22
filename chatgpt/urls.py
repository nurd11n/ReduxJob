from django.urls import path
from .views import *

urlpatterns = [
    path('', ChatBotAPIView.as_view(), name='chatbot'),
]