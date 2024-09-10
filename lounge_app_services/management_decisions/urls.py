from django.urls import path
from .views import leave_approval, search_users

urlpatterns = [
    path('leave_approval/', leave_approval, name='leave-approval'),
]

htmx_urlpatterns = [
    path('leave_approval/<str:action>/<int:pk>/', leave_approval, name='change-leave-status'),
    path('leave_approval/search-users/', search_users, name='search-users'),
]

urlpatterns += htmx_urlpatterns