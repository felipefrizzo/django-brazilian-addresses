from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from addresses.models import (
    State, City, Neighborhood, Street
)


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = (
            'id', 'name', 'initials', 'created_at', 'updated_at')


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


class StreetSerializer(ModelSerializer):
    state = serializers.CharField(source='get_state_initials')
    city = serializers.CharField(source='get_city_name')
    neighborhood = serializers.CharField(source='get_neighborhood_name')
    street_name = serializers.CharField(source='name')

    class Meta:
        model = Street
        fields = (
            'id', 'street_name', 'zipcode', 'neighborhood',
            'city', 'state', 'created_at', 'updated_at'
        )
