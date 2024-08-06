from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'flats', views.FlatViewSet, 'flat')
router.register(r'bookings', views.BookingViewSet, 'booking')

urlpatterns = [
    path('api/', include(router.urls)),
]