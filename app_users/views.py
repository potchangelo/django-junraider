from django.http import HttpRequest
from django.shortcuts import render

from app_users.forms import RegisterForm

# Create your views here.
def register(request: HttpRequest):
    form = RegisterForm()
    context = {"form": form}
    return render(request, "app_users/register.html", context)
