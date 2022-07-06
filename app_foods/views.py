from django.http import HttpRequest
from django.shortcuts import render
from app_foods.forms import FavoriteFoodForm
from app_foods.models import Food
from app_users.models import UserFavoriteFood

# Create your views here.


def foods(request: HttpRequest):
    all_foods = Food.objects.order_by("-is_premium")
    context = {"foods": all_foods}
    return render(request, "app_foods/foods.html", context)


def food(request: HttpRequest, food_id):
    one_food = None
    is_favorited = False
    try:
        one_food = Food.objects.get(id=food_id)
        if request.user.is_authenticated:
            user_favorite_food = UserFavoriteFood.objects.get(
                user=request.user,
                food=one_food
            )
            is_favorited = user_favorite_food is not None
    except:
        print("หาไม่เจอ หรือเธอไม่มี")

    form = FavoriteFoodForm()
    context = {
        "food": one_food,
        "form": form,
        "is_favorited": is_favorited
    }
    return render(request, "app_foods/food.html", context)
