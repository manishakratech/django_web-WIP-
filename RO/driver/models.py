from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Driver(models.Model):
    driver_name = models.CharField(max_length=100)
    driver_id = models.CharField(max_length=50)
    driver_email = models.EmailField()
    driver_password = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.driver_password = make_password(self.driver_password)
        super().save(*args, **kwargs)

    def check_password(self, password):
        return check_password(password, self.driver_password)

class CustomerOrder(models.Model):
    store = models.IntegerField()
    date = models.CharField(max_length=255)
    vehicle = models.CharField(max_length=255)
    shift = models.CharField(max_length=255)
    waypoints = models.TextField()
    summary = models.TextField()
    route = models.TextField()

    class Meta:
        managed = False
        db_table = 'customer_order'