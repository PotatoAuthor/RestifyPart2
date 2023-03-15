from django.urls import path
from .views import ReservationCreateView, ReservationCancelView, ReservationConfirmCancelView

app_name = "reservations"

urlpatterns = [
    path('create/', ReservationCreateView.as_view(), name='create_reservation'),
    path('<int:pk>/cancel/', ReservationCancelView.as_view(), name='cancel_reservation'),
    path('<int:pk>/confrimcancel/', ReservationConfirmCancelView.as_view(), name='confirm_cancel_reservation'),
]
