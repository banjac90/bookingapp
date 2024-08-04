from django.test import TestCase
from .models import Flat, Booking
from .views import FlatViewSet, BookingViewSet
from rest_framework.test import APIRequestFactory
from .serializers import FlatSerializer, BookingSerializer

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
        self.view = FlatViewSet.as_view({'get': 'list'})
        self.url = '/flat/'

    def test_flat_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

class BookingViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = BookingViewSet.as_view({'get': 'list'})
        self.url = '/booking/'

    def test_booking_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

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
        self.booking = Booking.objects.create(flat = self.flat, check_in="2024-08-03", check_out="2024-08-05")
        self.serializer = BookingSerializer(self.booking)
        self.expected_data = {"id": self.booking.id, "flat_name": "Flat1", "check_in": "2024-08-03", "check_out": "2024-08-05", "previous_booking_id": None}

    def test_booking_serializer(self):
        self.assertEqual(self.serializer.data, self.expected_data)

