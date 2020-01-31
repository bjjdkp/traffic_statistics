from django.contrib import admin
from .models import Users, TrafficInfo

# Register your models here.

admin.site.register(TrafficInfo)
admin.site.register(Users)
