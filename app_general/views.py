from django.shortcuts import render
from app_foods.models import Food

# Create your views here.

def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')

def subscription(request):
    all_foods = Food.objects.order_by('-is_premium')
    context = {'foods': all_foods}
    return render(request, 'app_general/subscription_form.html', context)

def subscription_thankyou(request):
    return render(request, 'app_general/subscription_thankyou.html')