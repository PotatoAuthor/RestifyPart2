from django.urls import path
from .views import ReservationCreateView

app_name = "reservations"

urlpatterns = [
    path('create/', ReservationCreateView.as_view(), name='create_reservation')
]
1