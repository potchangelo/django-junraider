from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from app_users.models import CustomUser


class EmailBackend(ModelBackend):
    def authenticate(self, request, username, password, **kwargs):
        print("Custom auth ... " + username)
        user: CustomUser = None
        try:
            user = CustomUser.objects.get(Q(username=username) | Q(email=username))
            is_wrong_password = not user.check_password(password)
            is_user_inactive = not self.user_can_authenticate(user)
            if is_wrong_password or is_user_inactive:
                raise Exception("Wrong password or inactive user")
        except:
            return None
        return user

    def get_user(self, user_id: int):
        user: CustomUser = None
        try:
            user = CustomUser.objects.get(id=user_id)
            if not self.user_can_authenticate(user):
                raise Exception("Inactive user")
        except:
            return None
        return user
