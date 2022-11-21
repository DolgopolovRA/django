from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', blank=True, unique=True)
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='Возраст')
    avatar = models.ImageField(upload_to='users', blank=True, null=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
