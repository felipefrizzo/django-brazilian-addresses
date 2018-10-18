import requests
from django.template.loader import render_to_string


class RequestsMixin:
    url = None
    headers = None
    template_name = None
    context = None

    def requests(self):
        template_name = self.get_template_name()
        url = self.get_url()
        headers = self.get_headers()

        body = render_to_string(template_name, self.context)
        return requests.post(url, data=body, headers=headers)

    def get_template_name(self):
        if self.template_name is None:
            raise NotImplemented
        return self.template_name

    def get_url(self):
        if self.url is None:
            return NotImplemented
        return self.url

    def get_headers(self):
        if self.headers is None:
            return {'Content-Type': 'application/json'}
        return self.headers
