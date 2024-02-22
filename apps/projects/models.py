from django.db import models
from django.contrib.auth import get_user_model
from apps.profiles.models import UserProfile

# Create your models here.

User = get_user_model()


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='projects')
    name_project = models.CharField(max_length=40)
    image_project = models.ImageField(upload_to='image_project/')
    description = models.TextField()
    link = models.CharField(max_length=70)
