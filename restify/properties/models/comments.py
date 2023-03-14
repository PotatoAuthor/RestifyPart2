from django.db import models
from django.contrib.auth import get_user_model
from .property import PropertyModel


# TODO Change - merge comment models
class UserComments(models.Model):
    commenter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    content = models.CharField()


class PropertyComments(models.Model):
    commenter = models.ForeignKey(get_user_model, on_delete=models.CASCADE, null=True)
    property = models.ForeignKey(PropertyModel, on_delete=models.CASCADE, null=True)
    content = models.CharField()
