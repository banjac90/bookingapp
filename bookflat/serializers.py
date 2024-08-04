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

    def get_previous_booking_id(self, obj):
        previous_booking = Booking.objects.filter(
            flat=obj.flat, check_out__lt=obj.check_in
        ).order_by('-check_out').first()
        return previous_booking.id if previous_booking else None
