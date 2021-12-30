from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Trip(models.Model):
    trip_name = models.CharField(max_length=120)
    user_tohost = models.ForeignKey(User, on_delete=models.CASCADE , related_name="users_host_trip" )
    user_ontrip  = models.ManyToManyField(User , related_name="users_ontrip")
    status = models.CharField(max_length=20 , default="current")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="user_notification"  )
    trip = models.ManyToManyField(Trip , related_name="userto_notify" )

class Spending(models.Model):
    trip = models.ForeignKey(Trip ,  on_delete=models.CASCADE , related_name="trip_spend")
    user = models.ForeignKey( User , on_delete=models.CASCADE , related_name="user_spend")
    description = models.CharField(null=False , max_length=300)
    spend = models.IntegerField(null=False)
    date_time = models.DateTimeField()  