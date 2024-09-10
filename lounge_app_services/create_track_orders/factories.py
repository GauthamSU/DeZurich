import factory
import random
import string
import factory.random
from faker import Faker
from datetime import datetime, timedelta, timezone
from .models import OrderDetails, OrderItem, status_choices
from lounge_app_services.menu.models import MenuItems
from lounge_app_services.menu.factories import MenuItemsFactory
from lounge_app_services.employee.factories import UserProfileFactory

fake = Faker()
# fake.date_time_between()
def id_generator():
    size=6
    chars=string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


class OrderDetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderDetails
        django_get_or_create = ('order_id',)

    
    employee = factory.SubFactory(UserProfileFactory)
    order_id = factory.LazyFunction(id_generator)
    

    table_num = factory.Faker('numerify', text='#%')

    # order_placed = factory.Faker('date_time_between',
    #                              start_date=datetime(year=2024, month=1, day=1),
    #                              end_date=datetime(year=2024, month=12, day=31),
    #                             #  tzinfo = timezone("Asia/Kolkata")
    #                             )
    

    order_prepared = factory.Faker('date_time_between',
                                   start_date = 'now',
                                   end_date = timedelta(hours=1),
                                   )
    order_completed = factory.Faker('date_time_between',
                                   start_date=factory.SelfAttribute('..order_prepared'),
                                   end_date = timedelta(minutes=30),
                                    )
    order_paid = factory.Faker('date_time_between',
                                start_date=factory.SelfAttribute('..order_completed'),
                                end_date = timedelta(hours=3),
                                )
    order_status = 'order_completed'

    @factory.post_generation
    def set_title(self, create, extracted, **kwargs):
        if create and extracted:
            for _ in range(random.randint(1,15)):
                menu_item = fake.random_element(elements=extracted)
                OrderItemFactory.create(order=self, product=menu_item)
        
class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem
    
    order = factory.SubFactory(OrderDetailsFactory)
    product = factory.SubFactory(MenuItemsFactory)
    quantity = factory.Faker('numerify', text='%')
    preference = factory.Faker('sentence', nb_words=10)
    
    @factory.post_generation
    def add_order(self, create, _, **__):
        if create:
            self.order.title.add(self)
            self.order.save()
            self.save()

