# iRating

- Um site para avaliar pedidos do ifood, onde cada usuário terá sua lista de pedidos, com suas avaliações, comentários e notas para cada item de cada loja.

## Regras

- precisa ter entre 5-10 entidades( tabelas)
- o sistema precisa ser acessado por apis
- o sistema precisa ter alguma tela em html, como um dashboard, graficos...
- precisa indexar dados no elasticsearch e api para buscar os dados
- precisa fazer web scraping em pelo menos 2 sites
- precisa processar os dados do web scraping e outros quaisquer processamentos usando celery e workers
- precisa ter upload de arquivo, pelo menos em uma entidade (tabela)
- incluir testes unitários e de integração para um coverage de no minimo 95%

## Funcionalidades

- Web scrap de determinada loja do ifood e do "???" para pegar todos os produtos
- Ranks e comparação dos seus pedidos
- Comentários sobre os pedidos
- Criar, editar e excluir pedidos
- Wishlist para futuros pedidos
- Cadastrar e separar as lojas por cidade
- Criação de usuário e senha para avaliaçẽs personalizadas
- Consumir por API
- Dashboard em html mostrando os dados
- Elastic Search
- Celery
- Upload de arquivos
- Testes
