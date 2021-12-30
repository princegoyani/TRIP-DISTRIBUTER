from django.contrib import admin
from .models import User , Trip, Notification , Spending

# Register your models here.
admin.site.register(User)
admin.site.register(Trip)
admin.site.register(Notification)
admin.site.register(Spending)