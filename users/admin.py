from django.contrib import admin
from .models import  CustomUser, LeaveBalance, LeavesRequest

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(LeaveBalance)
admin.site.register(LeavesRequest)
