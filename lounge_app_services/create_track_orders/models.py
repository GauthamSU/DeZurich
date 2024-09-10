import random
import string
from django.db import models
from lounge_app_services.menu.models import MenuItems
from lounge_app_services.employee.models import UserProfile
from django.utils import timezone



status_choices = (('order_placed', 'Order Placed'), ('order_prepared', 'Order Prepared'), ('order_completed', 'Order Completed'), ('order_paid', 'Order Paid'))


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class OrderDetails(models.Model):
    employee = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.ManyToManyField('OrderItem', blank=True)
    order_id = models.CharField(max_length=6, null=True, blank=True, unique=True, default=id_generator)
    table_num = models.IntegerField(null=True, blank=True)
    order_total = models.FloatField(null=True, blank=True)
    order_placed = models.DateTimeField(auto_now_add=True)
    order_prepared = models.DateTimeField(null=True, blank=True)
    order_completed = models.DateTimeField(null=True, blank=True)
    order_paid = models.DateTimeField(null=True, blank=True)
    total_quantity = models.IntegerField(null=True, blank=True)
    order_status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True, default='order_placed')
    
    def __str__(self):
        
        return f"{self.order_id} - {self.employee.user.username}"
    
    def __repr__(self):
        return f"{self.order_id}"


    def save(self, *args, **kwargs):
        # while OrderDetails.objects.filter(order_id=self.order_id).exists():
        #     self.order_id = id_generator()
        
        total_order_quantity, total_order_price = self.get_order_total_quantity()
        if total_order_quantity and total_order_price:
            self.total_quantity = total_order_quantity
            self.order_total = total_order_price
                
        # if self.order_status == 'order_completed':
        #     self.order_completed = timezone.now()

        super().save(*args, **kwargs)


    def get_order_total_quantity(self):
        try:
            items = self.title.all()
            if items:
                total_quantity = sum([item.quantity for item in items])
                total_price = sum([item.order_price for item in items])
                return total_quantity, total_price
        except ValueError:
            return None, None
        return None, None

    class Meta:
        ordering =['-order_placed']
        verbose_name = "Order details"
        verbose_name_plural = "Order details"

    

class OrderItem(models.Model):
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    preference = models.CharField(max_length=100, default='', null=True, blank=True)
    order_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.product.title
    
    def __repr__(self):
        if not self.order is None:
            return f"{self.order.order_id}"
        return 'None'
    
    def save(self, *args, **kwargs):
        self.order_price = int(self.quantity) * self.product.price
        return super().save(*args, **kwargs)
    

# class OrderItemCart(models.Model):
