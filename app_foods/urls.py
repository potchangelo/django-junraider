from django.urls import path

from app_foods import views

urlpatterns = [
    path("", views.foods, name="foods"),
    path("<int:food_id>", views.food, name="food"),
    path("<int:food_id>/favorite", views.favorite_food, name="favorite_food"),
    path("<int:food_id>/unfavorite", views.unfavorite_food, name="unfavorite_food"),
]
