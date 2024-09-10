from django.core.management.base import BaseCommand
from lounge_app_services.menu.models import MenuItems
from lounge_app_services.create_track_orders.factories import OrderDetailsFactory
from lounge_app_services.employee.factories import UserProfileFactory, EmployeeLeaveFactory
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = "Generates dummy users data for the website"
    

    def create_dummy_users(self, size=20):
        return UserProfileFactory.create_batch(size=size)
    
    def create_employee_leaves(self, elements, batch_size=10):
        all_leaves = []
        for _ in range(batch_size):
            employee = fake.random_element(elements=elements)
            leaves = EmployeeLeaveFactory.create_batch(employee=employee, size=random.randint(1,5))
            all_leaves.append(list(set(list(leaves))))
        return all_leaves
    
    def create_order_items(self, elements, batch_size=20):
        order_details = []
        menu_items = MenuItems.objects.all()
        for _ in range(batch_size):
            employee = fake.random_element(elements=elements)
            order = OrderDetailsFactory.create(employee=employee, set_title=menu_items)
            order_details.append(order)
        return order_details
        

    def handle(self, *args, **options):
        users_data = self.create_dummy_users()
        self.create_employee_leaves(elements=users_data)
        self.create_order_items(elements=users_data)
        