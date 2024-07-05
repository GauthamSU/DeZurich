from django.urls import path
from .views import workspace_view

urlpatterns = [
    path('', workspace_view, name='workspace'),
]