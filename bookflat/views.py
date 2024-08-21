from rest_framework import viewsets, filters
from .serializers import FlatSerializer, BookingSerializer
from .models import Flat, Booking
from django.db.models import OuterRef, Subquery

class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

class BookingViewSet(viewsets.ModelViewSet):   
    serializer_class = BookingSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['check_in']   

    def get_queryset(self):
        previous_booking_id = Booking.objects.filter(
            flat_id = OuterRef('flat_id'),
            check_out__lt = OuterRef('check_in')        
        ).order_by('-check_out').values('id')[:1]

        main_query = Booking.objects.annotate(
            previous_booking_id = Subquery(previous_booking_id)            
        ).select_related('flat').order_by('flat', 'check_in')

        ordering = self.request.query_params.get('ordering', None)
        if ordering:
            main_query = main_query.order_by(ordering)

        return main_query


