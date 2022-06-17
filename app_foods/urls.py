from django.urls import path
from app_foods import views

urlpatterns = [
    path("", views.foods, name="foods"),
    path("<int:food_id>", views.food, name="food"),
]
