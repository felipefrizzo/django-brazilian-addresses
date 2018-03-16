from django.urls import path, include
from rest_framework import routers

from django_brazilian_addresses.addresses.views import CountryView

router = routers.SimpleRouter()
router.register(r'countries', CountryView)

urlpatterns = [
    path('', include(router.urls))
]
