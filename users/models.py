from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email_confirmation_token = models.CharField(max_length=64, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.email_confirmation_token:
            self.email_confirmation_token = default_token_generator.make_token(self)
        super().save(*args, **kwargs)
