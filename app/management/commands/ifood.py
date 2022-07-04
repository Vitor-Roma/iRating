from django.core.management.base import BaseCommand
from app.tasks import scrap_products


class Command(BaseCommand):
    def handle(self, *args, **options):
        for page in self.get_page_list():
            print(page)
            scrap_products.delay(page)

    def get_page_list(self):
        page_list = [
            'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/five-burgers-freguesia-de-jacarepagua/9d041a66-51ee-4c7a-8e2e-9524076f7bf2',
            'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/outback---metropolitano-jacarepagua/9b4b068e-dd01-4e6d-8069-70e707b80490',
            'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/mcdonalds---shopping-metropolitano-barra-da-tijuca/a6450fe5-e1d5-4560-9ac4-6ed8971011af',
            'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/burger-king---shopping-met-barra-barra-da-tijuca/47300a96-e638-4bdf-89ed-a5dc33b49f6b',
            'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/subway-rio-2-jacarepagua/0556693a-53d1-4827-8c8f-319e8a317d88',
        ]
        return page_list
