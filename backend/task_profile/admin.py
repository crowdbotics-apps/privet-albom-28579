from django.contrib import admin
from .models import TaskerProfile, CustomerProfile, Notification, InviteCode

admin.site.register(Notification)
admin.site.register(InviteCode)
admin.site.register(CustomerProfile)
admin.site.register(TaskerProfile)

# Register your models here.
