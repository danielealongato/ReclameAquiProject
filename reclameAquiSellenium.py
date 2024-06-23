from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime
import time

# Configuração do WebDriver
chrome_options = Options()

# chrome_options.add_argument("--headless")  # Executar em modo headless, sem abrir a janela do navegador
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL da página do INSS no Reclame Aqui
url = 'https://www.reclameaqui.com.br/empresa/inss/'
driver.get(url)

#maximizar a tela
driver.maximize_window()
# Listas para armazenar os dados coletados
titulos = []
conteudos = []

#scrolar a página
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

#aceitar os cookies
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/a[1]').click()
#abrir mais reclamações
driver.find_element(By.XPATH,'//*[@id="box-complaints-read-all"]').click()
driver.find_element(By.XPATH,'//*[@id="box-complaints-read-all"]').click()
# Função para coletar reclamações de uma página
def coletar_reclamacoes():
    reclamacoes = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]/main/section[2]/div[2]/div[2]')
    for reclamacao in reclamacoes:
        try:
            # Coletar o título
            titulo = reclamacao.find_element(By.TAG_NAME, 'h4').text.strip()
            titulos.append(titulo)

            # Coletar o conteúdo
            conteudo = reclamacao.find_element(By.TAG_NAME, 'p').text.strip()
            conteudos.append(conteudo)

        except Exception as e:
            print(f"Erro ao processar uma reclamação: {e}")


# Coletar reclamações da primeira página
coletar_reclamacoes()

# Navegar pelas páginas seguintes e coletar reclamações
while True:
    try:
        # Tentar encontrar o botão "Próxima página"
        next_button = driver.find_element(By.XPATH, '//a[contains(@class, "sc-15vff5z-0")]')
        next_button.click()

        # Esperar a página carregar
        time.sleep(5)

        # Coletar reclamações da nova página
        coletar_reclamacoes()
    except Exception as e:
        print("Não foi possível encontrar o botão de próxima página ou não há mais páginas.")
        break

# Criar um DataFrame com os dados coletados
df = pd.DataFrame({
    'Titulo': titulos,
    'Conteudo': conteudos
})

# Salvar os dados em um arquivo CSV
df.to_csv('reclamacoes_inss.csv', index=False, encoding='utf-8-sig')

# Encerrar o WebDriver
driver.quit()

print('Dados salvos com sucesso no arquivo reclamacoes_inss.csv')
