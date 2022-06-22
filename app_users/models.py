from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    address = models.TextField(default="", blank=True)
    phone = models.CharField(max_length=15, default="", blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
