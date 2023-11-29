from django.urls import path
from .views import signup, user_login, user_logout, user_profile, profile_card

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('employee_profile/', profile_card, name='profile_card'),
]