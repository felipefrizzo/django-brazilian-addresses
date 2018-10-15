import requests
from django.conf import settings
from django.template.loader import render_to_string

DEFAULT_CORREIO_URL = """
https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl
"""


class RequestsMixin:
    url = getattr(settings, 'CORREIO_URL', DEFAULT_CORREIO_URL)
    headers = {'Content-Type': 'application/xml'}
    template_name = None
    context = None

    def requests(self):
        template_name = self.get_template_name()

        body = render_to_string(template_name, self.context)
        return requests.post(self.url, data=body, headers=self.headers)

    def get_template_name(self):
        if self.template_name is None:
            raise NotImplemented
        return self.template_name
