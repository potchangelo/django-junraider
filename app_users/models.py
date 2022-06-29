from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):
    address = models.TextField(default="", blank=True)
    phone = models.CharField(max_length=15, default="", blank=True)
    user = models.OneToOneField("app_users.CustomUser", on_delete=models.CASCADE)
