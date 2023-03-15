from django.db import models
from django.contrib.contenttypes.models import ContentType


class Notifications(models.Model):
    sender_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    sender_id = models.PositiveIntegerField()
    receiver_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    receiver_id = models.PositiveIntegerField()
    reservation = models.BooleanField()
    cancellation = models.BooleanField()

