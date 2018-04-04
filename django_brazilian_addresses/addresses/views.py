from rest_framework.viewsets import ReadOnlyModelViewSet

from django_brazilian_addresses.addresses.models import Country, State, City, \
    Neighborhood, StreetType, Street
from django_brazilian_addresses.addresses.serializers import \
    CountrySerializer, StateSerializer, CitySerializer, \
    NeighborhoodSerializer, StreetTypeSerializer, StreetSerializer


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
    filter_fields = ('state',)

    def paginate_queryset(self, queryset):
        qs = super(CityView, self).paginate_queryset(queryset)
        state = self.request.query_params.get('state', None)
        initials = self.request.query_params.get('initials', None)

        if state is not None or initials is not None:
            return None
        return qs

    def get_queryset(self):
        qs = super(CityView, self).get_queryset()
        initials = self.request.query_params.get('initials', None)

        if initials is not None:
            return City.objects.filter(state__initials=initials)
        return qs


class NeighborhoodView(ReadOnlyModelViewSet):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer


class StreetTypeView(ReadOnlyModelViewSet):
    queryset = StreetType.objects.all()
    serializer_class = StreetTypeSerializer
    pagination_class = None


class StreetView(ReadOnlyModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
