from django.test import TestCase
from .models import Flat, Booking
from .views import FlatViewSet, BookingViewSet
from rest_framework.test import APIRequestFactory, APIClient
from .serializers import FlatSerializer, BookingSerializer
from datetime import date
from django.urls import reverse

# Models test case
class FlatTestCase(TestCase):
    def setUp(self):
        Flat.objects.create(name="Flat1")

    def test_flat_name(self):
        flat = Flat.objects.get(name="Flat1")
        self.assertEqual(flat.name, "Flat1")

class BookingTestCase(TestCase):
    def setUp(self):
        flat = Flat.objects.create(name="Flat1")
        Booking.objects.create(flat=flat, check_in="2024-08-03", check_out="2024-08-05")

    def test_booking_flat(self):
        flat = Flat.objects.get(name="Flat1")
        booking = Booking.objects.get(flat=flat)
        self.assertEqual(booking.flat.name, "Flat1")

# Views test case
class FlatViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.view = FlatViewSet.as_view({'get': 'list'})
        self.url = self.client.get(reverse('flat-list'))

    def test_flat_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

class BookingViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = BookingViewSet.as_view({'get': 'list'})        
        self.client = APIClient()
        self.url = self.client.get(reverse('booking-list'))

        #Booking data
        self.flat1 = Flat.objects.create(name="Flat 1")
        self.flat2 = Flat.objects.create(name="Flat 2")        
        self.booking1 = Booking.objects.create(flat=self.flat1, check_in=date(2024, 1, 1), check_out=date(2024, 1, 5))
        self.booking2 = Booking.objects.create(flat=self.flat1, check_in=date(2024, 2, 10), check_out=date(2024, 2, 15))
        self.booking3 = Booking.objects.create(flat=self.flat1, check_in=date(2024, 3, 20), check_out=date(2024, 3, 30))        
        self.booking4 = Booking.objects.create(flat=self.flat2, check_in=date(2024, 2, 1), check_out=date(2024, 2, 5))
        self.booking5 = Booking.objects.create(flat=self.flat2, check_in=date(2024, 8, 5), check_out=date(2024, 8, 15))

    def test_booking_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_queryset(self):
        response = self.client.get(reverse('booking-list'))     
        print(self.booking1)
        fla1_first_booking = response.data['results'][0]
        booking1 = BookingSerializer(self.booking1)

        self.assertEqual(fla1_first_booking, booking1.data)
        self.assertEqual(fla1_first_booking['previous_booking_id'], None)

        flat1_second_booking = response.data['results'][1]

        self.assertEqual(flat1_second_booking['previous_booking_id'], self.booking1.id)
        
        flat2_second_booking = response.data['results'][4]

        self.assertEqual(flat2_second_booking['previous_booking_id'], self.booking4.id)

    def test_ordering_check_in(self):
        response = self.client.get(reverse('booking-list'), {'ordering': 'check_in'})        
        results = response.data['results']
        if len(results) > 1:
            for i in range(len(results) - 1):
                self.assertLessEqual(results[i]['check_in'], results[i+1]['check_in'])
        
# Serializers test case
class FlatSerializerTestCase(TestCase):
    def setUp(self):
        self.flat = Flat.objects.create(name="Flat1")
        self.serializer = FlatSerializer(self.flat)
        self.expected_data = {"id": self.flat.id, "name": "Flat1"}
    
    def test_flat_serializer(self):
        self.assertEqual(self.serializer.data, self.expected_data)

class BookingSerializerTestCase(TestCase):
    def setUp(self):
        self.flat = Flat.objects.create(name="Flat1")
        self.booking = Booking.objects.create(flat = self.flat, check_in=date(2024, 8, 3), check_out=date(2024, 8, 5))
        self.serializer = BookingSerializer(self.booking)
        self.expected_data = {"id": self.booking.id, "flat_name": "Flat1", "check_in": "2024-08-03", "check_out": "2024-08-05", "previous_booking_id": None}

    def test_booking_serializer(self):        
        self.assertEqual(self.serializer.data, self.expected_data)

 
