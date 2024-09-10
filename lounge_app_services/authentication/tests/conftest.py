import pytest
from lounge_app_services.authentication.factories import UserFactory, GroupFactory


# @pytest.fixture
# def get_or_create_groups():
#     return (GroupFactory(),)

@pytest.fixture
def create_users():
    size = 10
    return [UserFactory.create(add_groups= (GroupFactory(),) ) for _ in range(size)]
    # return UserFactory.create_batch(size)