from django.urls import path, include
from rest_framework import routers

from django_brazilian_addresses.addresses.views import CountryView, \
    StateView, CityView, NeighborhoodView, StreetTypeView

router = routers.SimpleRouter()
router.register(r'countries', CountryView)
router.register(r'states', StateView)
router.register(r'cities', CityView)
router.register(r'neighborhoods', NeighborhoodView)
router.register(r'street_types', StreetTypeView)

urlpatterns = [
    path('', include(router.urls))
]
