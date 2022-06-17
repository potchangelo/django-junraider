from django.urls import path
from app_general import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("subscription", views.subscription, name="subscription"),
    path(
        "subscription/thankyou",
        views.subscription_thankyou,
        name="subscription_thankyou",
    ),
]
