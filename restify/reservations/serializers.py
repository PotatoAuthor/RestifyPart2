from django.shortcuts import render
from rest_framework.serializers import ModelSerializer
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Reservation


# from django_filters.rest_framework import DjangoFilterBackend0

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'user',
            'status',
            'property',
            'start_date',
            'end_date'
        ]


class ReservationSerializerCreate(ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'user',
            'status',
            'property',
            'start_date',
            'end_date'
        ]

    def create(self, validated_data):
        Reservation.objects.create( )