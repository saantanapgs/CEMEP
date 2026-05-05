from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from login_credentials import user, password

# Definindo o navegador
options = Options()
options.add_argument(r"C:\Users\Cemep.sejuc\AppData\Local\Google\Chrome\User Data")
# Definindo perfil do Chrome
options.add_argument("profile-directory=Profile 1")
driver = webdriver.Chrome(options=options)

# Adicionando um delay para realizar cada passo da automação
wait = WebDriverWait(driver, 10)

driver.get("https://chronos.synergye.com.br/index.php?r=site/login")

login_user = wait.until(
  EC.presence_of_element_located((By.ID, "LoginForm_username"))
).send_keys(user)

login_password = wait.until(
  EC.presence_of_element_located((By.ID, "LoginForm_password"))
).send_keys(password)

btn = wait.until(
    EC.element_to_be_clickable((By.XPATH,"//input[@type='submit']"))
)
btn.click()

input("23")