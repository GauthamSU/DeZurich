from django.urls import path
from .views import initiate_order, track_order

urlpatterns = [
    path('place-order/', initiate_order, name='place-order'),
    path('track-order/', track_order, name="track-order"),
]