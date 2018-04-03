from django.urls import path, include
from rest_framework import routers

from django_brazilian_addresses.addresses.views import CountryView, \
    StateView, CityView

router = routers.SimpleRouter()
router.register(r'countries', CountryView)
router.register(r'states', StateView)
router.register(r'cities', CityView)

urlpatterns = [
    path('', include(router.urls))
]
