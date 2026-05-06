from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from login_credentials import user, password

#print("Acessando o site")
def chronos_login():
  # Definindo o navegador
  options = Options()
  options.add_argument(r"--user-data-dir=C:\selenium_profile")
  driver = webdriver.Chrome(options=options)

  # Adicionando um delay para realizar cada passo da automação
  wait = WebDriverWait(driver, 10)

  driver.get("https://se.synergye.com.br/index.php?r=site/login")

  login_user = wait.until(
    EC.presence_of_element_located((By.ID, "LoginForm_username"))
  )
  login_user.send_keys(user)

  login_password = wait.until(
    EC.presence_of_element_located((By.ID, "LoginForm_password"))
  )
  login_password.send_keys(password)

  login_btn = wait.until(
      EC.element_to_be_clickable((By.XPATH,"//input[@type='submit']"))
  )
  login_btn.click()

  # Entrando no menu Operacional para acessar o link 'Pessoa monitorada'
  operational_reference = wait.until(
      EC.element_to_be_clickable((By.XPATH, "//li[contains(@class,'dir')]//a[contains(., 'Operacional')]"))
  )
  operational_reference.click()

  monitored_reference = wait.until(
      EC.element_to_be_clickable((By.XPATH, "//a[@href='/index.php?r=pessoa']"))
  )
  monitored_reference.click()

  return driver, wait
# Pesquisando o nome do monitorado que consta no arquivo renomeado pelo main.py
def searching_monitored(driver, wait, cleaned_name):
  monitored_name_reference = wait.until(
      EC.element_to_be_clickable((By.ID, "Pessoa_pessoa_nome"))
  )
  monitored_name_reference.send_keys(cleaned_name)
  input("...")
