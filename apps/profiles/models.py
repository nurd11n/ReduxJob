from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

User = get_user_model()


class UserProfile(models.Model):
    id =  models.AutoField(primary_key=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    languages = models.CharField(max_length=256, blank=True)
    programming_languages = models.CharField(max_length=256, blank=True)
    education = models.TextField(blank=True)
    stack = models.CharField(max_length=50, blank=True)
    about = models.TextField(blank=True)
    age = models.PositiveIntegerField(blank=True, default=18)
    work_experience = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    profile_image = models.ImageField(blank=True, upload_to='profile_image/')

    def __str__(self):
        return self.user.email


class CompanyProfile(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
    about_company = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    direction = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='company/')

    def __str__(self):
        return f'{self.user.email}'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(f"User {instance.email} was created: {created}")
    if created:
        if User.objects.filter(type_user='Company'):
            CompanyProfile.objects.create(user=instance)
        elif User.objects.filter(type_user='Human'):
            UserProfile.objects.create(user=instance)
