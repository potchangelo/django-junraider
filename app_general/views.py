from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app_foods.models import Food
from .models import Subscription

# Create your views here.

def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')

def subscription(request):
    # POST
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        food_ids = request.POST.getlist('food_id')
        accepted = request.POST.get('accepted')

        if accepted == 'yes':
            new_sub = Subscription(name=name, email=email)
            new_sub.save()
            if len(food_ids) > 0:
                selected_foods = Food.objects.filter(id__in=food_ids)
                new_sub.food_set.set(selected_foods)
            return HttpResponseRedirect(reverse('subscription_thankyou'))
        
        all_foods = Food.objects.order_by('-is_premium')
        context = {
            'foods': all_foods, 'please_accepted': 'กรุณาติ๊กถูกตรงข้อตกลงเพิ่มเติมด้วย', 
            'values': request.POST, 'food_ids': list(map(int, food_ids))
        }
        return render(request, 'app_general/subscription_form.html', context)

    # GET
    all_foods = Food.objects.order_by('-is_premium')
    context = {'foods': all_foods}
    return render(request, 'app_general/subscription_form.html', context)

def subscription_thankyou(request):
    return render(request, 'app_general/subscription_thankyou.html')