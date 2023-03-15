from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Reservation
from .serializers import ReservationSerializer
from django.db.models import Q

# Create your views here.


class ReservationCreateView(generics.CreateAPIView):
    serializer_class = ReservationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            property_id = serializer.validated_data['property'].id
            start_date = serializer.validated_data['start_date']
            end_date = serializer.validated_data['end_date']

            # Check if there are any existing reservations for the property
            # in the same time frame
            existing_reservations = Reservation.objects.filter(
                Q(property_id=property_id),
                Q(start_date__lte=start_date, end_date__gte=start_date) |
                Q(start_date__lte=end_date, end_date__gte=end_date) |
                Q(start_date__gte=start_date, end_date__lte=end_date),
                ~Q(status='cancelled')
            )

            if existing_reservations:
                return Response(
                    {'error': 'A reservation for this property already exists in the selected time frame.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
