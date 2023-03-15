from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .serializers import PropertySerializer
from .models.property import PropertyModel
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CreatePropertyView(generics.CreateAPIView):
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class UpdatePropertyView(generics.RetrieveAPIView, generics.UpdateAPIView):
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated,]
    def get_object(self):
        return get_object_or_404(PropertyModel, pk=self.kwargs['pk'])
    
class DeletePropertyView(generics.DestroyAPIView):
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated,]
    def get_object(self):
        return get_object_or_404(PropertyModel, pk=self.kwargs['pk'])