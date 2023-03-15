from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Reservation
from properties.models.property import PropertyModel
from .serializers import ReservationSerializer
from django.db.models import Q


# Create your views here.


class ReservationCreateView(generics.CreateAPIView):
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        # Set status to 'pending' before saving
        serializer.save(status='pending_awaiting_confirmation')

        # Check if there are any existing reservations for the property
        # in the same time frame
        property_id = serializer.validated_data['property'].id
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']
        existing_reservations = Reservation.objects.filter(
            Q(property_id=property_id),
            Q(start_date__lte=start_date, end_date__gte=start_date) |
            Q(start_date__lte=end_date, end_date__gte=end_date) |
            Q(start_date__gte=start_date, end_date__lte=end_date),
            ~Q(status='cancelled')
        )

        if existing_reservations:
            raise serializers.ValidationError(
                'A reservation for this property already exists in the selected time frame.'
            )


class ReservationPagination(PageNumberPagination):
    page_size = 10


class ReservationListView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    pagination_class = ReservationPagination

    def get_queryset(self):
        queryset = Reservation.objects.all()

        # Filter by user type - host or guest
        user_type = self.request.query_params.get('user_type', None)
        if user_type == 'host':
            queryset = queryset.filter(property__owner=self.request.user)
        elif user_type == 'guest':
            queryset = queryset.filter(user=self.request.user)

        # Filter by reservation status
        request_status = self.request.query_params.get('status', None)
        if request_status is not None:
            queryset = queryset.filter(status=request_status)

        return queryset


class ReservationUpdateView(generics.UpdateAPIView):
    queryset = Reservation.objects.filter(status='pending_awaiting_confirmation')
    serializer_class = ReservationSerializer

    def patch(self, request, *args, **kwargs):
        reservation_id = kwargs.get('pk')
        reservation = self.get_object()
        owner = request.user

        if owner != reservation.property.owner:
            return Response({'error': 'You are not authorized to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

        status = request.data.get('status')
        if status not in ('confirmed', 'denied'):
            return Response({'error': 'Invalid status.'}, status=status.HTTP_400_BAD_REQUEST)

        reservation.status = status if status == 'confirmed' else 'terminated'
        reservation.save()
        serializer = self.serializer_class(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReservationCancelView(generics.UpdateAPIView):
    serializer_class = ReservationSerializer

    def update(self, request, *args, **kwargs):
        reservation = get_object_or_404(Reservation, id=self.kwargs.get('pk'))

        # Check if the user making the request is the same as the user who made the reservation
        if request.user != reservation.user:
            return Response(
                {'error': 'You do not have permission to cancel this reservation.'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Check if the reservation has already been cancelled or terminated
        if reservation.status in ('cancelled', 'terminated', 'cancelled_awaiting_confirmation'):
            return Response(
                {'error': 'This reservation has already been cancelled, awaiting confirmation, or terminated.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Update the status of the reservation to 'cancelled_awaiting_confirmation'
        reservation.status = 'cancelled_awaiting_confirmation'
        reservation.save()

        serializer = self.get_serializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReservationConfirmCancelView(generics.UpdateAPIView):
    serializer_class = ReservationSerializer

    def update(self, request, *args, **kwargs):
        reservation = get_object_or_404(Reservation, id=self.kwargs.get('pk'))

        # Check if the user making the request is the owner of the property
        property_owner = reservation.property.owner
        if request.user != property_owner:
            return Response(
                {'error': 'Only the owner of the property can confirm the cancellation of a reservation.'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Check if the reservation has already been cancelled or terminated
        if reservation.status in ['cancelled', 'terminated']:
            return Response(
                {'error': 'This reservation has already been cancelled or terminated.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the reservation is still awaiting confirmation
        if reservation.status != 'cancelled_awaiting_confirmation':
            return Response(
                {'error': 'This reservation is not awaiting confirmation.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Update the status of the reservation to 'cancelled'
        reservation.status = 'cancelled'
        reservation.save()

        # Update the availability of the property for the cancelled reservation's date range
        reservation_property = reservation.property
        reservation_property.update_availability(reservation.start_date, reservation.end_date)

        serializer = self.get_serializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReservationDenyCancelView(generics.UpdateAPIView):
    serializer_class = ReservationSerializer

    def update(self, request, *args, **kwargs):
        reservation = get_object_or_404(Reservation, id=self.kwargs.get('pk'))

        # Check if the user making the request is the owner of the property
        property_owner = reservation.property.owner
        if request.user != property_owner:
            return Response(
                {'error': 'Only the owner of the property can deny the cancellation of a reservation.'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Check if the reservation has already been cancelled or terminated
        if reservation.status in ['cancelled', 'terminated']:
            return Response(
                {'error': 'This reservation has already been cancelled or terminated.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the reservation is still awaiting confirmation
        if reservation.status != 'cancelled_awaiting_confirmation':
            return Response(
                {'error': 'This reservation is not awaiting confirmation.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Update the status of the reservation to 'cancelled'
        reservation.status = 'confirmed'
        reservation.save()

        # Update the availability of the property for the cancelled reservation's date range
        reservation_property = reservation.property
        reservation_property.update_availability(reservation.start_date, reservation.end_date)

        serializer = self.get_serializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)
