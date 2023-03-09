from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model

class CustomUser(AbstractUser):
    pass

    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    phone_num = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
