import factory
from faker import Faker
from .models import *
from django.utils.text import slugify


fake = Faker()

def create_sentences():
    return " ".join(fake.sentences(nb=5))


class MenuItemsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MenuItems
        django_get_or_create = ('slug_title',)

    title = factory.Faker('sentence', nb_words=10)
    description = factory.LazyFunction(create_sentences)
    price = factory.Faker('numerify', text='#%#.##')
    is_non_veg = factory.Faker('boolean', chance_of_getting_true=50)
    category = factory.Iterator([cat[0] for cat in CATEGORY_CHOICES])
    sub_category = factory.Faker('random_element', elements=[subcat[0] for subcat in SUBCAT_CHOICES])
    slug_title = factory.LazyAttribute(lambda o: slugify(o.title + ' ' + str(o.sub_category) + ' ' + str(o.is_non_veg)))

