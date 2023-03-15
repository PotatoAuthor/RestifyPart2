from rest_framework import serializers
from .models.property import PropertyModel

class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyModel
        fields = ['pics', 'address', 'country', 'start_date', 
                  'end_date', 'num_guests', 'num_beds', 'num_baths', 
                  'amenities', 'description']
        
    def create(self, validated_data):
        validated_data['owner'] = self.context.get('request').user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)