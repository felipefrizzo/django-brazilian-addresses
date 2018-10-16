# Django Brazilian Addresses
[![Build Status](https://travis-ci.org/felipefrizzo/django-brazilian-addresses.svg?branch=master)](https://travis-ci.org/felipefrizzo/django-brazilian-addresses)  
A django client library for Brazilian Correios API's, current solution available to find addresses by zipcode, calculate the shipping service and tracking.

## How to develop ?
In progress...

## Installation
Django Brazilian Addresses works with Django 1.9+.

To install it, simply:  
`pip install django-brazilian-address`  

Then add it to your INSTALLED_APPS on your setting.py and on your urls.py:  
```
settings.py

INSTALLED_APPS = [  
    # ...
    'addresses',
]

urls.py
from django.urls import path, include

urlpatterns = [
    # ...
    path('addresses/', include('addresses.urls'))
]

```

And run a simple load data with brazilian states: `python manage.py address_loaddata`

## TODO  
* Calculate the shipping service

## Author
This django library was created in 2018 by [Felipe Frizzo]('http://felipefrizzo.github.io')

## License
The MIT License (MIT)