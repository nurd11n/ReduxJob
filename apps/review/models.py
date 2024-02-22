from django.db import models
from django.contrib.auth import get_user_model
from apps.post.models import Forum

# Create your models here.

User = get_user_model()


class Comment(models.Model):
    body = models.TextField(verbose_name='Description')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='comments')
    files = models.FileField(upload_to='comment_files/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}, {self.body}'


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.author}{self.forum}'

