import pandas as pd
from selenium import webdriver
import time
import urllib
from selenium.webdriver.common.by import By

contatos_df = pd.read_excel("Teste.xls")       # importa contatos da planilha Enviar.xls
print(contatos_df)

navegador = webdriver.Chrome()                 # Abre navegador Chrome
#navegador = webdriver.Chrome("chromedriver.exe")
navegador.get('https://web.whatsapp.com/')

while len(navegador.find_elements(By.ID,"side")) < 1: # Aguarda que seja feito login com o QR Code
    time.sleep(1)

# já estamos com o login feito no whatsapp web
for i, mensagem in enumerate(contatos_df['Mensagem']):
        pessoa = contatos_df.loc[i, "Pessoa"]
        numero = contatos_df.loc[i, "Número"]
        texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        navegador.get(link)

        while len(navegador.find_elements(By.ID,'side')) < 1:
            time.sleep(2)

        print ("Aqui.")
        while len (navegador.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')) < 1:
            time.sleep (2)

        print ("Aqui!!!!!")
        time.sleep(3)
        while len (navegador.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')) < 1:
            time.sleep(2)

        print ("Aqui!!!!!!!!!!!!!!!!!!!!!!!!")
        navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        time.sleep(3)


navegador.quit()