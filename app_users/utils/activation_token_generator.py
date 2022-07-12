from django.contrib.auth.tokens import PasswordResetTokenGenerator

from app_users.models import CustomUser


class ActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: CustomUser, timestamp: int) -> str:
        return "{}{}{}".format(user.id, timestamp, user.is_active)


activation_token_generator = ActivationTokenGenerator()
