import pytest
from lounge_app_services.employee.factories import UserProfileFactory, EmployeeLeaveFactory

# @pytest.fixture
# def create_users(db):
#     size = 10
#     return [UserFactory.create(add_groups=[GroupFactory()]) for _ in range(size)]
#     # return UserFactory.create_batch(size)


@pytest.fixture
def create_user_profile():
    return UserProfileFactory()


@pytest.fixture
def create_employee_leave():
    employee_leave = EmployeeLeaveFactory()
    print(employee_leave.leave_start_date, employee_leave.leave_end_date)
    return employee_leave