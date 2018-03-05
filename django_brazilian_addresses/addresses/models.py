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
