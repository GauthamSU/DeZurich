from django.urls import path
from .field_validations import check_username, check_password1, check_password2, check_email


urlpatterns = [
    path('check-username/', check_username, name="check-username"),
    path('check-email/', check_email, name="check-email"),
    path('check-password1/', check_password1, name="check-password1"),
    path('check-password2/', check_password2, name="check-password2"),
    
]