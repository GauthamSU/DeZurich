from rest_framework import serializers
from .models import OrderDetails, OrderItem
from lounge_app_services.menu.models import MenuItems
from lounge_app_services.employee.models import UserProfile



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['title', 'category', 'sub_category']

class OrderItemSerializer(serializers.ModelSerializer):
    product = MenuItemSerializer()
    class Meta:
        model = OrderItem
        # fields = '__all__'
        exclude = ['order', 'id']


class OrderSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    # The default related name of a ManyToManyField is modelname_set.
    items = OrderItemSerializer(many=True, read_only=True, source='orderitem_set')
    class Meta:
        model = OrderDetails
        exclude = ['order_completed', 'order_prepared', 'order_paid', 'title']
        include = ['items']

