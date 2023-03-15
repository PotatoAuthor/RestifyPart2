from django.db import models
from django.contrib.auth import get_user_model
from properties.models.property import PropertyModel


class Reservation(models.Model):
    STATUS_CHOICES = (
        ('pending_awaiting_confirmation', 'Pending - Awaiting Confirmation'),
        ('confirmed', 'Confirmed'),
        ('cancelled_awaiting_confirmation', 'Cancelled - Awaiting Confirmation'),
        ('cancelled', 'Cancelled'),
        ('terminated', 'Terminated'),
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=31, choices=STATUS_CHOICES)
    property = models.ForeignKey(PropertyModel, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
