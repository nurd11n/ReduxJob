from django.urls import path, include
from .views import CommentView, LikeView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('comments', CommentView)
router.register('likes', LikeView)

urlpatterns = [
    path('', include(router.urls)),
]