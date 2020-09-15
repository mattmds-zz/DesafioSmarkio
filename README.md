# Desafio Smarkio

Teste automatizado E-commerce

Teste criado para o Desafio Smarkio QA jr.

Ferramentas utilizadas: Selenium e ChromeDriver
Linguagem: Phyton
Site para teste: https://www.submarino.com.br/

Funcionalidade 1: Localizar produto em site
Como usuário
Quero buscar um produto no site
Para saber se a loja o comercializa

Cenário 1: Produto Encontrado
Dado que estou com o site aberto
Quando digito o produto no campo de busca e clico no botão pesquisar
Então será carregada uma página com os produtos correspondentes

Cenário 2: Produto não Encontrado
Dado que estou com o site aberto
Quando digito o produto no campo de busca e clico no botão pesquisar
Então será carregada uma página informando que o produto não foi localizado

Funcionalidade 2: Adicionar Produto ao Carrinho
Como usuário
Quero adicionar o produto encontrado no carrinho
Para finalizar minha compra

Cenário 1: Produto Adicionado ao carrinho
Dado que já localizei o produto
Quando clico no botão comprar
Então o produto é adicionado ao carrinho de compras

Cenário 2: Produto não Adicionado ao carrinho
Dado que já localizei o produto
Quando clico no botão comprar
Então um erro é gerado
