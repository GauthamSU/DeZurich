from django.contrib import admin
from .models import UserProfile, EmployeeLeave

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'customer_name', 'gender', 'city']
    
    def customer_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    customer_name.short_description = 'Customer Name'


class EmployeeLeaveAdmin(admin.ModelAdmin):
    list_display = ['employee', 'leave_type', 'leave_start_date', 'leave_end_date', 'date_difference', 'is_approved']

    def date_difference(self, obj):
        return obj.date_difference()


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmployeeLeave, EmployeeLeaveAdmin)