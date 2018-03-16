from rest_framework.viewsets import ReadOnlyModelViewSet

from django_brazilian_addresses.addresses.models import Country
from django_brazilian_addresses.addresses.serializers import CountrySerializer


class CountryView(ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = None
