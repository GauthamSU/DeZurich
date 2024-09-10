import pytest
import factory
from faker import Faker
from datetime import datetime, timedelta
from lounge_app_services.authentication.factories import UserFactory, GroupFactory
from .models import UserProfile, EmployeeLeave, state_choices, gender_choices, leave_choices

fake = Faker()

today = datetime.today()


def get_zipcode():
    return fake.numerify('######')

@pytest.mark.django_db
def get_group():
    return (GroupFactory(),)


class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile
        django_get_or_create = ('user',)
    
    user = factory.SubFactory(UserFactory, add_groups=get_group)
    address = factory.Faker('street_address', locale='en_IN')
    phone_number = factory.Faker('phone_number', locale='en_IN')
    city = factory.Faker('city', locale='en_IN')
    state = factory.Faker('random_element', elements=[g[0] for g in state_choices])
    gender = factory.Faker('random_element', elements=[g[0] for g in gender_choices])
    zipcode = factory.LazyFunction(get_zipcode)



class EmployeeLeaveFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmployeeLeave
        # django_get_or_create = ('employee',)

    
    employee = factory.SubFactory(UserProfileFactory)
    leave_type = factory.Faker('random_element', elements=[leave[0] for leave in leave_choices])
    leave_details = factory.Faker('sentence', nb_words=10)
    leave_start_date = factory.Faker('date_between', 
                                     start_date=datetime(year=2024, month=1, day=1).date(),
                                     end_date=datetime(year=2024, month=12, day=30).date()
                                     )
    
    leave_end_date = factory.Faker('date_between', 
                                     start_date=factory.SelfAttribute('..leave_start_date'),
                                     end_date=datetime(year=2024, month=12, day=30).date()
                                    )
    is_approved = factory.Faker('boolean', chance_of_getting_true=25)
    revision = factory.Faker('sentence', nb_words=10)


    