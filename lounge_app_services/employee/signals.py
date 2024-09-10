from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from .models import UserProfile

def employee_profile(sender, instance, created, **kwargs):
    if created:
        user_instance = UserProfile.objects.create(user=instance)
        print(user_instance)

post_save.connect(employee_profile, sender=get_user_model())
