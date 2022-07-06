from django import forms
from app_users.models import UserFavoriteFood


class FavoriteFoodForm(forms.ModelForm):
    class Meta:
        model = UserFavoriteFood
        fields = ["level"]
        widgets = {"level": forms.RadioSelect}
