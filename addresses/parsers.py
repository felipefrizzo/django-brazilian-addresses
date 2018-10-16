import xml.etree.ElementTree as Et

from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import NotFound

from addresses.models import State, City, \
    Neighborhood, Street


def parser_get_zipcode_request(request) -> object:
    if not request.ok:
        return None

    tree = Et.fromstring(request.text).find('.//return')

    initials = tree.findtext('uf')
    city = tree.findtext('cidade')
    neighborhood = tree.findtext('bairro')
    zipcode = tree.findtext('cep')
    street = tree.findtext('end')

    try:
        state = State.objects.get(initials=initials)
    except State.DoesNotExist:
        raise NotFound({'state': _('State does not exists.')})

    try:
        city = City.objects.get(name=city, state=state)
    except City.DoesNotExist:
        if not neighborhood and not street:
            return City.objects.create(name=city, zipcode=zipcode, state=state)
        else:
            city = City.objects.create(name=city, state=state)

    try:
        neighborhood = Neighborhood.objects.get(name=neighborhood, city=city)
    except Neighborhood.DoesNotExist:
        neighborhood = Neighborhood.objects.create(
            name=neighborhood, city=city
        )

    try:
        street = Street.objects.get(zipcode=zipcode)
    except Street.DoesNotExist:
        street = Street.objects.create(
            name=street, zipcode=zipcode, neighborhood=neighborhood
        )
    return street
