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
    country = models.ForeignKey(
        'Country', on_delete=models.CASCADE, verbose_name='country')
    created_at = models.DateTimeField(
        'created at', auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        'updated at', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name
