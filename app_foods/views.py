from django.http.response import HttpResponse
from django.shortcuts import render

all_foods = [
    { 'id': 1, 'title': 'Red Spicy', 'price': 299, 'isPremium': False },
    { 'id': 2, 'title': 'Blue Iceberg', 'price': 299, 'isPremium': False },
    { 'id': 3, 'title': 'Premium Black Choco', 'price': 399, 'isPremium': True },
]

# Create your views here.
def foods(request):
    context = { 'foods': all_foods }
    return render(request, 'app_foods/foods.html', context)

def food(request, food_id):
    return render(request, 'app_foods/food.html')