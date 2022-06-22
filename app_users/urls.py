from django.urls import include, path

from app_users import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register", views.register, name="register"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile", views.profile, name="profile")
]
