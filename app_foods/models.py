from django.db import models

# Create your models here.


class Food(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    special_price = models.IntegerField(null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    promotion_end_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image_relative_url = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return "{} (id: {})".format(self.title, self.id)
