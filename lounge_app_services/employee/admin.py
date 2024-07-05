from django.contrib import admin
from .models import UserProfile, EmployeeLeave

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'gender', 'city']
    

admin.site.register(UserProfile)
admin.site.register(EmployeeLeave)