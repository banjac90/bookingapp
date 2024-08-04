from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'flats', views.FlatViewSet)
router.register(r'bookings', views.BookingViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]