# Django Brazilian Addresses
[![Build Status](https://travis-ci.org/felipefrizzo/django-brazilian-addresses.svg?branch=master)](https://travis-ci.org/felipefrizzo/django-brazilian-addresses)  
A django client library for Brazilian Correios API's, current solution available to find addresses by zipcode, calculate the shipping service and tracking.

## Documentation  
See REQUIREMENTS in the [setup.py](https://github.com/felipefrizzo/django-brazilian-addresses/blob/master/setup.py) file for additional dependencies:
* Python 3.4 or higher
* Django 1.9 or higher
* Django Rest Framework 3.8 or higher
* Requests 2.19 or higher

#### Installation
* run `pip install django-brazilian-addresses`
* add `addresses` to your `INSTALLED_APPS`
* add `addresses.urls` to your `urls.py`
* run `python manage.py address_loaddata` to load brazilian states

#### Configurations
```python
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

## TODO  
* Calculate the shipping service

## How to develop ?
1. Clone repository.
2. Create a virtualenv with python 3.4 or higher and activate.
3. Install dependencies.
4. Run tests.

```shell
$ git clone https://github.com/felipefrizzo/django-brazilian-addresses.git
$ cd django-brazilian-addresses
$ python -m venv .venv
$ source .venv/bin/activete
$ pip install pipenv && pipenv install --dev
$ python manage.py test
```

## Author
This django library was created in 2018 by [Felipe Frizzo]('http://felipefrizzo.github.io')

## License
The MIT License (MIT)