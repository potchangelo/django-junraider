from datetime import datetime, timedelta
from django.http import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app_general.forms import SubscriptionModelForm

# Create your views here.


def home(request: HttpRequest):
    return render(request, "app_general/home.html")


def about(request: HttpRequest):
    return render(request, "app_general/about.html")


def subscription(request: HttpRequest):
    # POST
    if request.method == "POST":
        form = SubscriptionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("subscription_thankyou"))
    else:
        form = SubscriptionModelForm()

    # GET
    context = {"form": form}
    return render(request, "app_general/subscription_form.html", context)


def subscription_thankyou(request: HttpRequest):
    return render(request, "app_general/subscription_thankyou.html")


def change_theme(request: HttpRequest):
    referer = request.headers.get("referer")
    if referer is not None:
        response = HttpResponseRedirect(referer)
    else:
        response = HttpResponseRedirect(reverse("home"))

    # Theme
    theme = request.GET.get("theme")
    if theme == "dark":
        expired_date = datetime.now() + timedelta(days=365)
        response.set_cookie("theme", "dark", expires=expired_date, samesite="Lax")
    else:
        response.delete_cookie("theme")

    return response
