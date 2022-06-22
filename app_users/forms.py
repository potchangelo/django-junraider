from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from app_users.models import Profile


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class ExtendedProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("address", "phone")
        labels = {
            "address": "ที่อยู่",
            "phone": "เบอร์โทรศัพท์",
        }
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3})
        }
