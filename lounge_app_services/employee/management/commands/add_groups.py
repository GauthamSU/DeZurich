from typing import Any
from guardian.shortcuts import assign_perm
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

default_groups = ['Kitchen Staff', 'Floor Staff', 'Management Staff']

class Command(BaseCommand):
    help = "Generates transactions for testing"
    
    def handle(self, *args, **options):
        for group in default_groups:
            Group.objects.get_or_create(name=group)
            