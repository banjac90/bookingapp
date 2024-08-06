from rest_framework import serializers
from .models import Flat, Booking

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    previous_booking_id = serializers.SerializerMethodField() #store the previous booking id
    flat_name = serializers.CharField(source='flat.name', read_only=True) 

    class Meta:
        model = Booking
        fields = ['id', 'flat_name', 'check_in', 'check_out', 'previous_booking_id']

    # Set the previous booking id to None if it is not available
    def get_previous_booking_id(self, obj):
        return getattr(obj, 'previous_booking_id', None)