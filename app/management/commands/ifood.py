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
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/lemax-hamburgueria----abelardo-bueno-barra-da-tijuca/1404b50d-b298-4f96-8feb-978e590bec0d',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/santa-marta-sucos---jacarepagua-jacarepagua/b5d33961-7a2d-4d58-8056-9404a61f391c',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/rao-burger---jacarepagua-freguesia-jacarepagua/ba0ccda3-a2fc-49a5-ba47-ed98085a5b5c',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/cachorro-quente-da-tia-jacarepagua/08411d9d-03bc-49e6-950c-1df86530b894',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/ex-touro---burger-parque-olimpico-barra-da-tijuca/36f1a5ca-1f55-4c90-b91f-49eb75061837',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/bob-beef---burger-metropolitano-jacarepagua/33c61a28-d31e-4135-8e83-a0aaab823372',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/neres-delivery-hamburgueria-taquara/f39075fe-0089-43d7-8119-86b37b286ce3',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/o-burgues---burger-parque-olimpico-barra-da-tijuca/12d329ce-3d6a-4fd0-bcf7-5fa155525487',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/o-burgues---burger-parque-olimpico-barra-da-tijuca/12d329ce-3d6a-4fd0-bcf7-5fa155525487',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/bob-smash---burger-metropolitano-jacarepagua/07d3dc48-1d46-4097-abda-e81ce97070a8',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/black-toro---shopping-uptown-gardenia-azul/e7291826-d540-45a4-bc10-af96bce0960d',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/comer-barato-taquara/0d67d75d-1e81-4668-9fb7-fa72eaca46b5',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/hamburgueria-puma-burguer-recreio-dos-bandeirantes/60b44c77-4f74-4842-94a9-ba475194a91a',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/baratissimo-rj-taquara/244bea43-cbc5-4697-ac77-a02d203777ed',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/comer-bem-e-barato-curicica/bdc55c2f-4c3f-48fd-ad9c-d61e20da8994',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/bella-pizzaria-jacarepagua/0b601faa-fa7e-4091-87b5-db8ef0627a36',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/tati---burgers-porcoes-e-acai-jacarepagua/be1bd225-3937-4733-87c6-d31757fa93c3',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/testa-burguer-recreio-dos-bandeirantes/4c277880-283c-48b5-aaa4-d4857b6a98ee',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/vini-lanches--petiscaria-taquara/885fdf16-4393-455b-a20e-28e0279d230c',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/flix-burger-recreio-dos-bandeirantes/20e9fb6e-a671-4b67-986d-facc74b1361f',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/lemax-hamburgueria---via-parque-barra-da-tijuca/beadb4bf-900f-4c54-b959-210865168267',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/padaria-santa-marta---jacarepagua-jacarepagua/c1436619-2998-40a9-8ea6-c42d79770729',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/subway-rio-2-jacarepagua/0556693a-53d1-4827-8c8f-319e8a317d88',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/taco-bell---metropolitano-barra-rj-jacarepagua/cb46f5a6-03f9-4e48-b3ea-30f6fafac879',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/nosso-crepe-freguesia-jacarepagua/324adf86-59f9-476d-bea7-f3524cf74d9f',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/billy-burger---cidade-jardim-jacarepagua/32e87f44-2e03-46e6-af89-e98d57f81036',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/acai-frut-mix-curicica/1a28ce5d-ab4e-4c97-8726-4bac98a1b7ec',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/porto-do-sabor-rio2-jacarepagua/a2589f8c-35b0-483b-a5ac-30c474d4487f',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/praca-do-suco-taquara/af9e1fc0-8fa7-4c8f-91d2-3f999da50c33',
            # 'https://www.ifood.com.br/delivery/rio-de-janeiro-rj/cabana-burger-barra-barra-da-tijuca/e1fe2c10-41c9-4f99-8ffe-8a1dc015f2e6',

        ]
        return page_list
