from .models import User
from django.contrib.auth.backends import BaseBackend


class LoginModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            if '@' in username:
                user = User.objects.get(email=username)
            else:
                try:
                    if username.isnumber():
                        user = User.objects.get(username=username)
                except User.DoesNotExist:
                    return None

        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)

        except User.DoesNotExist:
            return None
