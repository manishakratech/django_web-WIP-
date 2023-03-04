from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from .models import Driver

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, driver_email=None, driver_password=None):
        try:
            driver = Driver.objects.get(driver_email=driver_email)
            if driver.check_password(driver_password):
                return driver
        except Driver.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Driver.objects.get(pk=user_id)
        except Driver.DoesNotExist:
            return None

