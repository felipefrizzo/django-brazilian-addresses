from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from django_brazilian_addresses.addresses.models import Country, State, City, \
    Neighborhood, StreetType, Street


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'created_at', 'updated_at')


class StateSerializer(ModelSerializer):
    country = serializers.CharField(source='get_country_name')

    class Meta:
        model = State
        fields = (
            'id', 'name', 'initials', 'country', 'created_at', 'updated_at')


class CitySerializer(ModelSerializer):
    state = serializers.CharField(source='get_state_name')

    class Meta:
        model = City
        fields = (
            'id', 'name', 'zipcode', 'ibge',
            'state', 'created_at', 'updated_at'
        )


class NeighborhoodSerializer(ModelSerializer):
    city = serializers.CharField(source='get_city_name')

    class Meta:
        model = Neighborhood
        fields = ('id', 'name', 'city', 'created_at', 'updated_at')


class StreetTypeSerializer(ModelSerializer):
    class Meta:
        model = StreetType
        fields = ('id', 'name', 'abbreviation', 'created_at', 'updated_at')


class StreetSerializer(ModelSerializer):
    state = serializers.CharField(source='get_state_initials')
    city = serializers.CharField(source='get_city_name')
    neighborhood = serializers.CharField(source='get_neighborhood_name')
    street_name = serializers.CharField(source='name')
    street_type = serializers.CharField(source='get_patio_type')

    class Meta:
        model = Street
        fields = (
            'id', 'street_type', 'street_name', 'zipcode', 'neighborhood',
            'city', 'state', 'is_grand_user', 'created_at', 'updated_at'
        )
