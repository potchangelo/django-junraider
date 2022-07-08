from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
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
    try:
        one_food = Food.objects.get(id=food_id)
    except:
        print("หาไม่เจอ หรือเธอไม่มี")

    form = FavoriteFoodForm()
    context = {
        "food": one_food,
        "form": form
    }
    return render(request, "app_foods/food.html", context)


@login_required
def favorite_food(request: HttpRequest, food_id):
    if request.method == "POST":
        form = FavoriteFoodForm(request.POST)
        if form.is_valid():
            obj, is_created = UserFavoriteFood.objects.update_or_create(
                user=request.user,
                food=Food(id=food_id),
                defaults={"level": form.cleaned_data.get("level")}
            )
            print("Create favorite" if is_created else "Update favorite")

    return HttpResponseRedirect(reverse("food", args=[food_id]))
