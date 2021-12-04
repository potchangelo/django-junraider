from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def foods(request):
    return render(request, 'app_foods/foods.html')

def food(request, food_id):
    return render(request, 'app_foods/food.html')