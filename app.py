from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

#acessar site com desafio
driver = webdriver.Chrome()
driver.get('https://rpachallenge.com/?lang=EN')
driver.maximize_window()
sleep(2)

# iniciar o desafio
btn_start = driver.find_element(By.XPATH, "//button [contains(text(),'Start')]")
btn_start.click()
sleep(2)

# extrair informações da planilha 

planilha = openpyxl.load_workbook("./challenge.xlsx")
planilha_info = planilha['Sheet1']

for linha in planilha_info.iter_rows(min_row=2, values_only=True):
    primeiro_nome, ultimo_nome, empresa, setor, endereco, email, telefone, desconsiderar = linha

    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, "//label[text()='Phone Number']/following-sibling::input").send_keys(telefone)
    driver.find_element(By.XPATH, "//label[text()='Company Name']/following-sibling::input").send_keys(empresa)
    driver.find_element(By.XPATH, "//label[text()='Last Name']/following-sibling::input").send_keys(ultimo_nome)
    driver.find_element(By.XPATH, "//label[text()='First Name']/following-sibling::input").send_keys(primeiro_nome)
    driver.find_element(By.XPATH, "//label[text()='Role in Company']/following-sibling::input").send_keys(setor)
    driver.find_element(By.XPATH, "//label[text()='Address']/following-sibling::input").send_keys(endereco)

    btn_enviar = driver.find_element(By.XPATH, "//input[@type='submit']")
    btn_enviar.click()
    sleep(3)

sleep(5)
driver.quit()

    