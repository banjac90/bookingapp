from rest_framework import viewsets
from .serializers import FlatSerializer, BookingSerializer
from .models import Flat, Booking

class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('flat', 'check_in') # Default order as requested :)
    serializer_class = BookingSerializer

