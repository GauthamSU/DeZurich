from django.urls import path
from .views import initiate_order, track_order, order_filter_view

urlpatterns = [
    path('place-order/', initiate_order, name='place-order'),
    path('track-order/', track_order, name="track-order"),
    path('place-order/filter/<str:category>/', order_filter_view, name="filter-order"),
]