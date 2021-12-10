from django.db import models

# Create your models here.


class Subscription(models.Model):
    STATUS = [
        ('unapproved', 'Unapproved'),
        ('banned', 'Banned'),
        ('approved', 'Approved')
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    status = models.CharField(
        max_length=15, choices=STATUS, default='unapproved')
    registered_at = models.DateTimeField(auto_now_add=True)