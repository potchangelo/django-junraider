# Generated by Django 4.0 on 2021-12-11 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0004_rename_ispremium_food_is_premium_and_more'),
        ('app_general', '0002_rename_registeredat_subscription_registered_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='food',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_foods.food'),
        ),
    ]
