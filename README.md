# iRating

## Introduction

- iRating é um applicativo em API onde voce pode fazer o web-scrap dos produtos de qualquer restaurante do ifood e salvar no seu database. (Atenção: ele não pega produtos de outros tipos de lojas do ifood, como mercado e etc...)
- Você pode criar diferentes profiles, cada profile podendo ter seus proprios reviews dos produtos e wishlist para futuros pedidos.

## Funcionalidades

- Web-scrap de qualquer restaurante do ifood (não funciona com mercado) para pegar todos os produtos disponíveis
- Reviews e comentários sobre produtos
- Wishlist para futuros pedidos
- Criação de usuário e senha para avaliaçẽs personalizadas
- Consumir por API
- Dashboard em html mostrando os dados

## Tecnologias

- Docker-Compose
- DockerFile
- MakeFile
- Elastic Search
- Celery
- Upload de arquivos
- Testes

## Instalação

```python
- Docker
- Docker Compose
- Makefile
- Postman (para melhor vizualização da api)
```


## Primeiros passos

- Renomeie seu arquivo '.env_sample' para '.env' para conectar ao banco de dados
- Abra o terminal na pasta raiz e siga os passos abaixo:

- Para fazer a instalação e construção dos containers, use o comando make all

```
make all 
```

- Depois rode o comando make build para fazer as migrates.

```
make build
```

- Pronto, tudo instalado. Nas proximas vezes, só precisará rodar o comando make run para subir os containers

```
make run
```

## Web-Scrapping

<img src='https://user-images.githubusercontent.com/105290851/192857465-e21e5dab-0e4b-45ec-898c-cae7324c3ead.png'>

- Para escolhar qual restaurante você quer fazer o web-scrap dos produtos, basta apenas colocar o link dele do ifood na 'page_list', localizada em app/management/commands/ifood.py.
- Pode ser apenas um link, ou uma lista de links, o web-scrapping será feito em toda a lista, seguindo a ordem em que foram colocados.

## Dashboard

<img src='https://user-images.githubusercontent.com/105290851/192857452-2d142c18-32b0-4903-a8e1-bda72c1434b8.png'>
<img src='https://user-images.githubusercontent.com/105290851/192857454-c7f4cffb-d151-44f6-bc71-2cbbb554940a.png'>

- Agora acessamos a Home page, um html básico para mostrar os dados que foram salvos no banco de dados no link: 0.0.0.0:8000
- Também podemos acessar a lista dos produtos no link '/products' ou clicando em 'products' no dashboard
- Os demais links nos levam direto para a página de API


## Para fazer os testes use o comando:

```
make test
```

## Para uma lista mais detalhada dos comandos, acesse o arquivo Makefile

<img src='https://user-images.githubusercontent.com/105290851/192859164-75dd727f-1f98-496e-b809-16f77d0fe5a9.png'>

## API End-Points

<img src='https://user-images.githubusercontent.com/105290851/192857458-9b73ad74-1e94-4a69-bd62-2bf5e6cf498d.png'>

- Ao usar o postman, você pode importar as Collections e o Environment da pasta Postman para facilitar seu acesso diretamente as APIs


<img src='https://user-images.githubusercontent.com/105290851/192857459-376861b8-8e52-420d-a2ac-e3ca5662648a.png'>


    0.0.0.0:8000 (Home page)
    0.0.0.0:8000/api/sign-up (Criar Usuário)
    0.0.0.0:8000/api/login (Pegar seu token de acesso)
    0.0.0.0:8000/api/profile/ (Acesso aos profiles)  
    0.0.0.0:8000/api/restaurants/ (Acesso aos restaurantes)  
    0.0.0.0:8000/api/products/ (Acesso aos produtos)  
    0.0.0.0:8000/api/rating/ (Acesso as reviews)  
    0.0.0.0:8000/api/wishlist/ (Acesso a wishlist)
