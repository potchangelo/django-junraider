# Generated by Django 4.0 on 2021-12-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Food",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=20)),
                ("price", models.IntegerField()),
                ("isPremium", models.BooleanField()),
                ("promotionEndAt", models.DateTimeField()),
            ],
        ),
    ]
