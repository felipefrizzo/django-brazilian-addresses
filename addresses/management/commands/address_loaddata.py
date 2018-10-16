from django.core.management import BaseCommand

from addresses.models import State


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.handle_states()

    def handle_states(self):
        states = [
            ['AC', 'Acre'],
            ['AL', 'Alagoas'],
            ['AM', 'Amazonas'],
            ['AP', 'Amapá'],
            ['BA', 'Bahia'],
            ['CE', 'Ceará'],
            ['DF', 'Distrito Federal'],
            ['ES', 'Espírito Santo'],
            ['GO', 'Goiás'],
            ['MA', 'Maranhão'],
            ['MG', 'Minas Gerais'],
            ['MS', 'Mato Grosso do Sul'],
            ['MT', 'Mato Grosso'],
            ['PA', 'Pará'],
            ['PB', 'Paraíba'],
            ['PE', 'Pernambuco'],
            ['PI', 'Piauí'],
            ['PR', 'Paraná'],
            ['RJ', 'Rio de Janeiro'],
            ['RN', 'Rio Grande do Norte'],
            ['RO', 'Rondônia'],
            ['RR', 'Roraima'],
            ['RS', 'Rio Grande do Sul'],
            ['SC', 'Santa Catarina'],
            ['SE', 'Sergipe'],
            ['SP', 'São Paulo'],
            ['TO', 'Tocantins'],
        ]

        for state in states:
            State.objects.get_or_create(name=state[1], initials=state[0])
