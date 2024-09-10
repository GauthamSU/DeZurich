import pytest
import factory
from .models import User
from faker import Faker
from django.contrib.auth.models import Group
from django.db.models.signals import post_save

fake = Faker()

domain_name = 'dezurich.com'

pytestmark = pytest.mark.django_db        

def generate_username():
    while True:
        username = fake.user_name()
        if len(username) >= 8:
            return username


def generate_password():
    return fake.password()


def generate_email():
    return fake.email(domain=domain_name)


# @pytest.mark.django_db
class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group
        django_get_or_create = ('name',)

    name = factory.Faker("random_element", elements=("Kitchen Staff", "Floor Staff"))

# @pytest.mark.django_db
@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.LazyFunction(generate_username)
    email = factory.LazyFunction(generate_email)
    password = factory.django.Password(generate_password())
    
    @factory.post_generation
    def add_groups(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            if callable(extracted):
                self.groups.add(*extracted())
            else:
                self.groups.add(*extracted)
            self.save()
            
            # self.save()
