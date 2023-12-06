from django.urls import path
from .views import initiate_order

urlpatterns = [
    path('place-order/', initiate_order, name='place-order'),
]