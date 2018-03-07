from django.core.exceptions import ValidationError
from django.db import models


class Country(models.Model):
    name = models.CharField('name', max_length=255)
    created_at = models.DateTimeField(
        'created at', auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        'updated at', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField('name', max_length=255)
    initials = models.CharField('initials', max_length=2)
    country = models.ForeignKey(
        'Country', on_delete=models.CASCADE, verbose_name='country')
    created_at = models.DateTimeField(
        'created at', auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        'updated at', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name


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


class StreetType(models.Model):
    name = models.CharField('name', max_length=15)
    abbreviation = models.CharField(
        'abbreviation', max_length=5, null=True, blank=True)
    created_at = models.DateTimeField(
        'created at', auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        'updated at', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField('name', max_length=255)
    zipcode = models.CharField('zipcode', max_length=8, null=True, blank=True)
    neighborhood = models.ForeignKey(
        'Neighborhood', on_delete=models.CASCADE, verbose_name='neighborhood')
    street_type = models.ForeignKey(
        'StreetType', on_delete=models.CASCADE, verbose_name='street type')
    is_grand_user = models.BooleanField('is grand user', default=False)
    created_at = models.DateTimeField(
        'created at', auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        'updated at', auto_now_add=True, auto_now=False)

    def __str__(self):
        return f'{self.get_street_type()} {self.name}'

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

    def get_street_type(self) -> str:
        return self.street_type.name
