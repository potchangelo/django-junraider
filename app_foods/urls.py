from django.urls import path
from . import views

urlpatterns = [
    path('', views.foods, name='foods'),
    path('1', views.food, name='food')
]