from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
import re
from rest_framework.exceptions import ValidationError


# Create your models here.

class UserManager(BaseUserManager):
    def _create(self, email, password, **extra_fields):
        if not email:
            raise ValueError(
                'Email not be not'
            )
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.create_activation_code()
        user.create_forgot_password_code()
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    type_choices = [
        ('Human', 'Human'),
        ('Company', 'Company'),
    ]
    type_user = models.CharField(max_length=7, choices=type_choices)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=20, blank=True)
    forgot_password_code = models.CharField(max_length=20, blank=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.id} {self.email}'

    def create_activation_code(self):
        code = get_random_string(length=5, allowed_chars='0123456789')
        self.activation_code = code

    def create_forgot_password_code(self):
        code = get_random_string(length=5, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.forgot_password_code = code

    def clean(self):
        if self.phone_number and not re.match(r'^\+?[0-9]+$', self.phone_number):
            raise ValidationError(_('Invalid phone number format'))
        super().clean()

