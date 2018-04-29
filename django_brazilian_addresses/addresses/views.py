from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import NotFound
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
            qs = City.objects.filter(state__initials=initials)
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
    filter_fields = ('zipcode',)

    def get_queryset(self):
        qs = super(StreetView, self).get_queryset()
        get_zipcode = self.request.query_params.get('zipcode', None)

        if get_zipcode is not None:
            qs = Street.objects.filter(zipcode=get_zipcode)
            if not qs:
                self.serializer_class = CitySerializer
                qs = City.objects.filter(zipcode=get_zipcode)
                if not qs:
                    raise NotFound({'street': _('Street cannot be found')})
        return qs
