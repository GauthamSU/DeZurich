import random
import string
from django.db import models
from menu.models import MenuItems
from employee.models import UserProfile


status_choices = (('order_placed', 'Order Placed'), ('order_prepared', 'Order Prepared'), ('order_completed', 'Order Completed'), ('order_paid', 'Order Paid'))

class OrderDetails(models.Model):
    title = models.ForeignKey(MenuItems, blank=True, null=True, on_delete=models.DO_NOTHING)
    order_id = models.CharField(max_length=6, null=True, blank=True, unique=True)
    employee = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.DO_NOTHING)
    table_num = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    preference = models.CharField(max_length=200, default='', null=True, blank=True)
    order_placed = models.DateTimeField(auto_now_add=True)
    order_total = models.IntegerField(null=True, blank=True)
    order_status = models.CharField(default='order_placed' ,choices=status_choices, max_length=20)

    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def save(self):
        if not self.order_id:
            # Generate ID once, then check the db. If exists, keep trying.
            self.order_id = self.id_generator()  
            while OrderDetails.objects.filter(order_id=self.order_id).exists():
                self.order_id = self.id_generator()
        super(OrderDetails, self).save()


    def __str__(self):
        return self.title

    