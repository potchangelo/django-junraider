from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app_users.forms import ExtendedProfileForm, RegisterForm, UserProfileForm
from app_users.models import CustomUser

# Create your views here.
def register(request: HttpRequest):
    # POST
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Register and wait for activation
            user: CustomUser = form.save(commit=False)
            user.is_active = False
            user.save()

            # login(request, user)

            # Build email body
            # ...

            # Send email
            email = EmailMessage(to=[user.email], subject="Activate account หน่อยครับ", body="กดยืนยันตัวตนซะดีๆ")
            email.send()

            # Change redirect to register thank you
            return HttpResponseRedirect(reverse("register_thankyou"))
    else:
        form = RegisterForm()

    # GET
    context = {"form": form}
    return render(request, "app_users/register.html", context)


def register_thankyou(request: HttpRequest):
    return render(request, "app_users/register_thankyou.html")


@login_required
def dashboard(request: HttpRequest):
    return render(request, "app_users/dashboard.html")

@login_required
def profile(request: HttpRequest):
    user = request.user

    # POST
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user)
        is_new_profile = False
        try:
            # Will be updated profile
            extended_form = ExtendedProfileForm(request.POST, instance=user.profile)
        except:
            # Will be created profile
            is_new_profile = True
            extended_form = ExtendedProfileForm(request.POST)

        if form.is_valid() and extended_form.is_valid():
            form.save()
            if is_new_profile:
                # Create profile
                profile = extended_form.save(commit=False)
                profile.user = user
                profile.save()
            else:
                # Update profile
                extended_form.save()
            return HttpResponseRedirect(reverse("profile"))
    else:
        form = UserProfileForm(instance=user)
        try:
            extended_form = ExtendedProfileForm(instance=user.profile)
        except:
            extended_form = ExtendedProfileForm()

    # GET
    context = {
        "form": form,
        "extended_form": extended_form
    }
    return render(request, "app_users/profile.html", context)
