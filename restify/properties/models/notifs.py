from django.db import models
from django.contrib.auth import get_user_model

class NotifModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    content = models.CharField()