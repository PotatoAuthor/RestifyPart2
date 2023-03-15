from django.db.models import Model, ImageField, CharField, DateField, IntegerField, ForeignKey, CASCADE
from django.contrib.auth import get_user_model


# Create your models here.

class PropertyModel(Model):
    pics = ImageField(upload_to='images/', blank=True, null=True)
    address = CharField(max_length=200)
    country = CharField(max_length=50)
    start_date = DateField()
    end_date = DateField()
    num_guests = IntegerField()
    num_beds = IntegerField()
    num_baths = IntegerField()
    amenities = CharField(max_length=500, blank=True, null=True)
    description = CharField(max_length=200, blank=True, null=True)
    owner = ForeignKey(get_user_model(), on_delete=CASCADE, null=True)
