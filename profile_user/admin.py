from django.contrib import admin

from .models import User_Profile, Notification

# Register your models here.

admin.site.register(User_Profile)
admin.site.register(Notification)