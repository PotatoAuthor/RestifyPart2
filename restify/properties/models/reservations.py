from django.db import models
from django.contrib.auth import get_user_model
from .property import PropertyModel

class ReservationModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    status = models.CharField()
    property = models.ForeignKey(PropertyModel, on_delete=models.CASCADE, null=True)