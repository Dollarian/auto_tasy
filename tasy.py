# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import undetected_chromedriver as uc
import time
import os

# Configurações do navegador
options = webdriver.ChromeOptions()

# Caminho para o diretório de dados do usuário do Chrome
user_data_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data')

# Nome do perfil que você deseja usar (por exemplo, "Profile 1" ou "Default")
profile_name = "Profile 1"

# Adiciona as opções para usar o perfil existente
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument(f"--profile-directory={profile_name}")

# Outras opções do Chrome
options.add_argument("--start-maximized")  # Inicia o navegador maximizado
options.add_argument("--disable-blink-features=AutomationControlled")  # Evita detecção de automação

# Inicializa o Chrome com o perfil especificado
driver = uc.Chrome(options=options, use_subprocess=True, headless=False)

# Aguarda 05 segundos antes de iniciar o processo de login
time.sleep(5)

# Variáveis do site
variables = [
    "https://tasyweb.spdm.org.br/#/login",  # URL de login
    "//input[@placeholder='User name']",    # Campo de usuário
    "//input[@placeholder='Password']",     # Campo de senha
    "input.btn-green.w-login-button.w-login-button--green"  # Seletor CSS para o botão de login
]

# Defina o usuário e senha diretamente no código
username = "usr_spaa"  # Substitua com o seu nome de usuário
password = "hospital@123"  # Substitua com a sua senha

# Configuração do stealth para evitar detecção
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
)

def logging_in():
    try:
        # Acessa a página de login
        print("Acessando a página de login...")
        driver.get(variables[0])

        # Preenche o campo de usuário
        print("Preenchendo o campo de usuário...")
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, variables[1])))
        user_field = driver.find_element(By.XPATH, variables[1])
        user_field.send_keys(username)

        # Preenche o campo de senha
        print("Preenchendo o campo de senha...")
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, variables[2])))
        password_field = driver.find_element(By.XPATH, variables[2])
        password_field.send_keys(password)

        # Clica no botão de login usando o seletor CSS correto
        print("Clicando no botão de login...")
        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, variables[3]))
        )
        login_button.click()

        # Coloca o navegador em tela cheia após o login
        print("Colocando o navegador em tela cheia...")
        driver.fullscreen_window()

    except TimeoutException:
        print("Erro: Tempo de espera excedido. Verifique os elementos da página.")
        # Verifica se há mensagens de erro na página
        try:
            error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'error-message')]").text
            print(f"Mensagem de erro: {error_message}")
        except NoSuchElementException:
            print("Nenhuma mensagem de erro encontrada.")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Executa a função de login
start_time = time.time()
logging_in()
end_time = time.time()

# Exibe o tempo de execução
print(f"Tempo total de execução: {end_time - start_time:.2f} segundos.")

# O navegador ficará aberto indefinidamente após o login, sem fechar
print("O navegador ficará aberto para inspeção. Pressione Ctrl+C para interromper o processo.")
while True:
    time.sleep(3600)  # Esse loop mantém o navegador aberto indefinidamente