from django.urls import path, include
from .views import signup, user_login, user_logout
from .field_validations import check_username

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('signup/', include('lounge_app_services.authentication.htmx_urls')),
    
]

