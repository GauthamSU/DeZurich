from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.validators import UnicodeUsernameValidator

class User(AbstractUser):
    
    email = models.EmailField("email address", blank=True, unique=True) 
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._meta.get_field('username').max_length = 20
        self._meta.get_field('username').validators = [UnicodeUsernameValidator(), MinLengthValidator(8), MaxLengthValidator(20)]
        self._meta.get_field('username').help_text = 'Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.'
        
    def __str__(self) -> str:
        return self.username
    