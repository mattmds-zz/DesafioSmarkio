from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

navegador = webdriver.Chrome() #inicialização do webdriver para o Google chrome
navegador.maximize_window() #maximizando janela

link = 'https://www.submarino.com.br/' #site de acesso
itembuscado = 'iphone'        #item a ser buscado no site
navegador.get(url= link)
campo_busca = navegador.find_element_by_css_selector('#h_search-input') #selecionando campo de busca da pagina

campo_busca.send_keys(itembuscado) #preenchendo campo de busca
sleep(2) #aguardar 2 segundos
botao_pesquisar = navegador.find_element_by_xpath('//*[@id="h_search-btn"]') #selecionando botão de busca
botao_pesquisar.click() #acionando botão de busca

#Teste de retorno de busca: Funcionalidade 1
if navegador.find_elements_by_css_selector('#content-middle > div:nth-child(6) > div > div > div'):
    #Cenário 1: Produto não encontrado
    sleep(3)
    print("Sem resultados de busca")
    navegador.quit()
else:
    #Cenário 2: Produto encontrado
    item = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content-middle > div:nth-child(6) > div > div > div > div.row.product-grid.no-gutters.main-grid > div:nth-child(1) > div > div.RippleContainer-sc-1rpenp9-0.dMCfqq > a > section > div.Info-bwhjk3-5.gWiKbT.ViewUI-sc-1ijittn-6.iXIDWU > div.TitleWrapper-sc-1wh9e1x-7.cOZQdh.ViewUI-sc-1ijittn-6.iXIDWU > h2')))
    item.click() #selecionando o produto escolhido
    sleep(2)
    botao_comprar = navegador.find_element_by_css_selector('#btn-buy > div')
    botao_comprar.click() #acionando botão comprar
    bota_continuar = navegador.find_element_by_css_selector('#btn-continue')
    bota_continuar.click() #acionando o botão continuar compra
    #Teste de envio ao Carrinho de Compras: Funcionalidade 2
    if navegador.find_element_by_css_selector('#app > section > section > div.productsandfreight__wrapper > div.basket-products'):
        #Cenário 1: Produto adicionado ao carrinho
        sleep(2)
        print("teste ok")
        sleep(2)
        navegador.quit()
    else:
        #Cenário 2: Produto não adicionado ao carrinho
        print("falha")
        navegador.quit()


