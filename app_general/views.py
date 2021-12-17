from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app_foods.models import Food
from app_general.forms import SubscriptionForm1
from .models import Subscription

# Create your views here.

def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')

def subscription(request):
    # POST
    if request.method == 'POST':
        form = SubscriptionForm1(request.POST)
        if form.is_valid():
            sub_data = form.cleaned_data
            new_sub = Subscription(name=sub_data['name'], email=sub_data['email'])
            new_sub.save()
            new_sub.food_set.set(sub_data['food_set'])
            return HttpResponseRedirect(reverse('subscription_thankyou'))
    else:
        form = SubscriptionForm1()
    
    # GET
    context = {'form': form}
    return render(request, 'app_general/subscription_form.html', context)

def subscription_thankyou(request):
    return render(request, 'app_general/subscription_thankyou.html')