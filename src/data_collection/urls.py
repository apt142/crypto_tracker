from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CurrencyViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"", CurrencyViewSet, basename="currency")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("currency/", include(router.urls)),
]
