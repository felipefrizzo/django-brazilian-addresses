from rest_framework.viewsets import ReadOnlyModelViewSet

from django_brazilian_addresses.addresses.models import Country, State, City
from django_brazilian_addresses.addresses.serializers import \
    CountrySerializer, StateSerializer, CitySerializer


class CountryView(ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = None


class StateView(ReadOnlyModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    pagination_class = None


class CityView(ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
