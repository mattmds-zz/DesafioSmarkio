# Desafio Smarkio

Teste automatizado E-commerce

<b>Teste criado para o Desafio Smarkio QA jr.</b>

Ferramentas utilizadas: Selenium e ChromeDriver<br>
Linguagem: Phyton<br>
Site para teste: https://www.submarino.com.br/

<b>Funcionalidade 1</b>: Localizar produto em site<br>
Como usuário<br>
Quero buscar um produto no site<br>
Para saber se a loja o comercializa

Cenário 1: Produto Encontrado<br>
Dado que estou com o site aberto<br>
Quando digito o produto no campo de busca e clico no botão pesquisar<br>
Então será carregada uma página com os produtos correspondentes

Cenário 2: Produto não Encontrado<br>
Dado que estou com o site aberto<br>
Quando digito o produto no campo de busca e clico no botão pesquisar<br>
Então será carregada uma página informando que o produto não foi localizado

Funcionalidade 2: Adicionar Produto ao Carrinho<br>
Como usuário<br>
Quero adicionar o produto encontrado no carrinho<br>
Para finalizar minha compra

Cenário 1: Produto Adicionado ao carrinho<br>
Dado que já localizei o produto<br>
Quando clico sobre ele, e em seguida nos botões comprar, e continuar<br>
Então o produto é adicionado ao carrinho de compras

Cenário 2: Produto não Adicionado ao carrinho<br>
Dado que já localizei o produto<br>
Quando clico sobre ele, e em seguida nos botões comprar, e continuar<br>
Então um erro é gerado
