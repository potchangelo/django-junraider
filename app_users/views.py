from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app_users.forms import ExtendedProfileForm, RegisterForm, UserProfileForm

# Create your views here.
def register(request: HttpRequest):
    # POST
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Register & Login
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
    else:
        form = RegisterForm()

    # GET
    context = {"form": form}
    return render(request, "app_users/register.html", context)


@login_required
def dashboard(request: HttpRequest):
    return render(request, "app_users/dashboard.html")

@login_required
def profile(request: HttpRequest):
    form = UserProfileForm()
    extended_form = ExtendedProfileForm()
    context = {
        "form": form,
        "extended_form": extended_form
    }
    return render(request, "app_users/profile.html", context)
