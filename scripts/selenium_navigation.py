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
  monitored_name_reference.send_keys(Keys.ENTER)

  # Clicando no botão para abrir o perfil do monitorado
  view_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='view']"))
  )
  view_btn.click()
  
  # Clicando na sessão de 'Arquivos'
  files_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='#arquivoPessoaTab']"))
  )
  files_btn.click()

  # Clicando para criar novo arquivo
  new_file_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[contains(@onclick, 'openFileModal')]"))
  )
  new_file_btn.click()

  # Expandindo o select chamado 'Categoria do Arquivo'
  inputs = driver.find_elements(By.XPATH, "//input[@aria-label='Categoria do Arquivo']")

  print(f"Quantidade encontrada: {len(inputs)}")

  for i, inp in enumerate(inputs):
    print(i, inp.is_displayed(), inp.is_enabled())

  # Clicando em 'Documentos' dentro do select
  documents_option = wait.until(
      EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Documentos')]"))
  )
  documents_option.click()

  file_name = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Nome do arquivo']"))
  )
  file_name.send_keys(file_name)

  input("...")
