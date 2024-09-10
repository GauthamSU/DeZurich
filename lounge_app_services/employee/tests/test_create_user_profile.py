import pytest
from lounge_app_services.employee.models import UserProfile, EmployeeLeave

@pytest.mark.django_db
def test_create_users_profile(create_user_profile):
    profile = UserProfile.objects.get(user__username=create_user_profile)
    
    assert profile.user == create_user_profile.user
    assert profile.zipcode == int(create_user_profile.zipcode)
    assert profile.address == create_user_profile.address
    assert profile.phone_number == create_user_profile.phone_number
    assert profile.city == create_user_profile.city
    assert profile.state == create_user_profile.state
    assert profile.gender == create_user_profile.gender
    assert profile.profile_pic.url == '/media/static/profile.png'


@pytest.mark.django_db
def test_create_employee_leave(create_employee_leave):
    employee = EmployeeLeave.objects.get(employee=create_employee_leave.employee)
    
    assert employee.leave_type == create_employee_leave.leave_type
    assert employee.leave_details == create_employee_leave.leave_details
    assert employee.leave_start_date == create_employee_leave.leave_start_date
    assert employee.leave_end_date == create_employee_leave.leave_end_date
    assert employee.is_approved == create_employee_leave.is_approved
    assert employee.revision == create_employee_leave.revision
