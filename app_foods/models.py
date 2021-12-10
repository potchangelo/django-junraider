from django.db import models

# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    specialPrice = models.IntegerField(null=True)
    isPremium = models.BooleanField(default=False)
    promotionEndAt = models.DateTimeField(null=True)
    description = models.TextField(null=True)