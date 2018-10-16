from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import resolve_url


class State(models.Model):
    name = models.CharField('name', max_length=255)
    initials = models.CharField('initials', max_length=2)
    created_at = models.DateTimeField(
        'created at', auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        'updated at', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        return resolve_url('state-detail', self.pk)


class City(models.Model):
    name = models.CharField('name', max_length=255)
    zipcode = models.CharField('zipcode', max_length=8, blank=True, null=True)
    ibge = models.CharField('ibge', max_length=10, blank=True, null=True)
    state = models.ForeignKey(
        'State', on_delete=models.CASCADE, verbose_name='state')
    created_at = models.DateTimeField(
        'created at', auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        'updated at', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

    def get_state_name(self) -> str:
        return self.state.name

    def get_absolute_url(self) -> str:
        return resolve_url('city-detail', self.pk)


class Neighborhood(models.Model):
    name = models.CharField('name', max_length=255)
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, verbose_name='city')
    created_at = models.DateTimeField(
        'created at', auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        'updated at', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

    def get_city_name(self) -> str:
        return self.city.name

    def get_absolute_url(self) -> str:
        return resolve_url('neighborhood-detail', self.pk)


class Street(models.Model):
    name = models.CharField('name', max_length=255)
    zipcode = models.CharField(
        'zipcode', max_length=8, null=True, blank=True
    )
    neighborhood = models.ForeignKey(
        'Neighborhood', on_delete=models.CASCADE, verbose_name='neighborhood')
    created_at = models.DateTimeField(
        'created at', auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        'updated at', auto_now_add=True, auto_now=False)

    def __str__(self):
        return f'{self.name}'

    def clean(self):
        if self.neighborhood.city.zipcode is None and \
                (not self.zipcode or self.zipcode is None):
            raise ValidationError({'zipcode': 'zipcode cannot be empty'})
        super(Street, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Street, self).save(*args, **kwargs)

        if not self.zipcode or self.zipcode is None:
            self.zipcode = self.neighborhood.city.zipcode
            self.save()

    def get_absolute_url(self) -> str:
        return resolve_url('street-detail', self.pk)

    def get_state_initials(self) -> str:
        return self.neighborhood.city.state.initials

    def get_city_name(self) -> str:
        return self.neighborhood.city.name

    def get_neighborhood_name(self) -> str:
        return self.neighborhood.name
