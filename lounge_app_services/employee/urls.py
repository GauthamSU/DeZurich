from django.urls import path
from .views import user_profile, profile_card, apply_leave, remove_leave_request
urlpatterns = [
    path('profile/', user_profile, name='profile'),
    path('employee_profile/', profile_card, name='profile_card'),
    path('employee_leave/', apply_leave, name='apply_leave'),
    path('remove_leave/', remove_leave_request, name='dummy_url'),
    path('remove_leave/<str:pk>/', remove_leave_request, name='remove_leave')
]

htmx_patterns = [
    path('employee_leave/<str:pk>/', apply_leave, name='particular_leave'),
]

urlpatterns += htmx_patterns