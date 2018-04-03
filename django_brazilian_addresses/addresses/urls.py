from django.urls import path, include
from rest_framework import routers

from django_brazilian_addresses.addresses.views import CountryView, StateView

router = routers.SimpleRouter()
router.register(r'countries', CountryView)
router.register(r'states', StateView)

urlpatterns = [
    path('', include(router.urls))
]
