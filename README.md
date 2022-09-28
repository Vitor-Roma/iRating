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

```
Caso seja a primeira vez usando esse container, precisaremos usar o código:
- make all (Somente para a primeira vez usando o código, para fazer a construção, instalação e subir o container) para as demais vezes, usar o make run.
- make run (Para subir o container)
- make build (Para fazer as migrates)
```

## Web-Scrapping

<img src=>

- Para escolhar qual restaurante você quer fazer o web-scrap dos produtos, basta apenas colocar o link dele do ifood na 'page_list', localizada em app/management/commands/ifood.py.
- Pode ser apenas um link, ou uma lista de links, o web-scrapping será feito em toda a lista, seguindo a ordem em que foram colocados.

## Dashboard

<img src=>

- Agora acessamos a Home page, um html básico para mostrar os dados que foram salvos no banco de dados no link: 0.0.0.0:8000
- Também podemos acessar a lista dos produtos no link '/products' ou clicando em 'products' no dashboard
- Os demais links nos levam direto para a página de API


## Para fazer os testes use o comando:

```
- make test
```

# API End-Points

- Ao usar o postman, você pode importar as Collections e o Environment da pasta Postman para facilitar seu acesso diretamente as APIs

<img src=>


    0.0.0.0:8000 (Home page)
    0.0.0.0:8000/api/sign-up (Criar Usuário)
    0.0.0.0:8000/api/login (Pegar seu token de acesso)
    0.0.0.0:8000/api/profile/ (Acesso aos profiles)  
    0.0.0.0:8000/api/restaurants/ (Acesso aos restaurantes)  
    0.0.0.0:8000/api/products/ (Acesso aos produtos)  
    0.0.0.0:8000/api/rating/ (Acesso as reviews)  
    0.0.0.0:8000/api/wishlist/ (Acesso a wishlist)
