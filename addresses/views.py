from django.utils.translation import ugettext_lazy as _
from requests import Timeout, ConnectionError, HTTPError
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from addresses.mixins import RequestsMixin
from addresses.models import State, City, Neighborhood, Street
from addresses.parsers import parser_get_zipcode_request
from addresses.serializers import (
    StateSerializer, CitySerializer, NeighborhoodSerializer, StreetSerializer
)


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


class StreetView(RequestsMixin, ReadOnlyModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    lookup_url_kwarg = 'zipcode'
    template_name = 'addresses/get_street_by_zipcode.xml'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_street(kwargs.get('zipcode'))
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_street(self, zipcode: str):
        if not zipcode.isdigit() or len(zipcode) != 8:
            raise ValidationError({
                'zipcode': _('Zip code must contain only 8 digits.')
            })
        self.context = {'zipcode': zipcode}
        try:
            request = self.requests()
        except ConnectionError as err:
            raise ValueError("ConnectionError", err)
        except Timeout as err:
            raise ValueError("Timeout", err)
        except HTTPError as err:
            raise ValueError("HTTPError", err)

        instance = parser_get_zipcode_request(request)
        if not instance:
            raise NotFound({'address': _('Address does not exists.')})

        if isinstance(instance, City):
            self.serializer_class = CitySerializer
        elif isinstance(instance, Street):
            self.serializer_class = StreetSerializer
        return instance
