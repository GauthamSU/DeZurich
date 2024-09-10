import pytest
from lounge_app_services.authentication.models import User
# from lounge_app_services.authentication.factories import UserFactory
from django.contrib.auth.models import Group


@pytest.mark.django_db
def test_create_users_model(create_users):
    users = User.objects.filter(username__in=create_users)
    print(create_users[0].groups)
    assert users.count() == len(create_users)
    assert all(
        [user.email != None for user in users]
    )
    assert all(
        [user.first_name != None for user in users]
    )
    assert all(
        [user.last_name != None for user in users]
    )
    assert all(
        [user.username != None for user in users]
    )
    
