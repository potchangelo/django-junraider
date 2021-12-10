from django.db import models

# Create your models here.

class Subscription(models.Model):
    class Status(models.TextChoices):
        UNAPPROVED = 'unapproved',
        BANNED = 'banned',
        APPROVED = 'approved'

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.UNAPPROVED)
    registered_at = models.DateTimeField(auto_now_add=True)