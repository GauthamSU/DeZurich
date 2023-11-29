from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfile

def employee_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('Profile Created')

post_save.connect(employee_profile, sender=User)
