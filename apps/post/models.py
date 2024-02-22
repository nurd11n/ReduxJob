from django.db import models
from django.contrib.auth import get_user_model
from apps.profiles.models import UserProfile, CompanyProfile

# Create your models here.


User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts')
    name = models.CharField(max_length=150)
    type_choices = [
        ('Work', 'Work'),
        ('Teams', 'Teams'),
    ]
    type_post = models.CharField(max_length=5, choices=type_choices)
    description = models.TextField()
    celery = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum')
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='forum')
    name = models.CharField(max_length=150)
    description = models.TextField()
    file = models.FileField(upload_to='forum_file/')


class ErCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ercode')
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ercode')
    name = models.TextField()
    description = models.TextField()
    file = models.FileField(upload_to='ercode_file/')


class CompanyPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_posts')
    profile = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='company_posts')
    name = models.CharField(max_length=150)
    type_choices = [
        ('Work', 'Work'),
        ('Teams', 'Teams'),
    ]
    type_post = models.CharField(max_length=5, choices=type_choices)
    description = models.TextField()
    celery = models.PositiveIntegerField()


class CompanyVacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_vacancy')
    profile = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='company_vacancy')
    title = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    celery = models.PositiveIntegerField()
    type_work_choices = [
        ('Work', 'Work'),
        ('Internship', 'Internship')
    ]
    type_work = models.CharField(max_length=10, choices=type_work_choices)
    type_choices = [
        ('Office', 'Office'),
        ('Online', 'Online'),
    ]
    type_employment = models.CharField(max_length=6, choices=type_choices)


class DitailUserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ditail_user_post')
    title = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ditail_user_post')
    body = models.TextField()


class DitailCompanyPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ditail_company_post')
    title = models.CharField(max_length=50)
    post = models.ForeignKey(CompanyPost, on_delete=models.CASCADE, related_name='ditail_company_post')
    body = models.TextField()


class DitailCompanyVacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ditail_company_vacancy')
    title = models.CharField(max_length=50)
    post = models.ForeignKey(CompanyVacancy, on_delete=models.CASCADE, related_name='ditail_company_vacancy')
    body = models.TextField()

