from django.db import models
from menu.models import MenuItems
from employee.models import UserProfile

# Create your models here.
class OrderDetails(models.Model):
    title = models.ForeignKey(MenuItems, blank=True, null=True, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.DO_NOTHING)
    table_num = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    preference = models.CharField(max_length=200, default='', null=True, blank=True)
    order_placed = models.DateTimeField(auto_now_add=True)
    order_total = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
