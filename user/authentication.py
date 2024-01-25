# from django.contrib.auth.models import User
from user.models import User

class EmailAuthBackend:
    """
    Authenticate using an e-mail address.
    """
    def authenticate(self, request, username=None, password=None):
        print(username, password)
        try:
            # print("in try")
            user = User.objects.get(email=username)
            print(user)
            if user.check_password(password):
                return user

            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None