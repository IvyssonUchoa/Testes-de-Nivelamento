import time
import zipfile
import urllib.request
from pathlib import Path

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

#########################################################################################

# Instala a versão compatível do chrome driver
chrome_service = Service(ChromeDriverManager().install())

# Definindo as opções do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--start-maximized")

# Obtem o caminho do diretório atual
current_path = Path(__file__).parent.resolve()

# Cria o driver do Chrome
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

#########################################################################################

def download_files(url):
    try:
        # Acessa o site
        driver.get(url)

        time.sleep(5)

        # Remove o overlay de desfoque da página
        safe_area = driver.find_element(By.TAG_NAME, 'body')
        ActionChains(driver).move_to_element(safe_area).click().perform()

        # Localiza o link para o primeiro anexo
        annex_1_xpath = '/html/body/div[2]/div[1]/main/div[2]/div/div/div/div/div[2]/div/ol/li[1]/a[1]' 
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, annex_1_xpath)))

        annex_1_link = driver.find_element(By.XPATH, annex_1_xpath).get_attribute('href')

        # faz o download do Anexo 1 para a pasta de download
        annex_1_path = current_path / "downloads/anexo_1.pdf"
        urllib.request.urlretrieve(annex_1_link, annex_1_path)

        # Localiza o link para o primeiro anexo
        annex_2_xpath = '/html/body/div[2]/div[1]/main/div[2]/div/div/div/div/div[2]/div/ol/li[2]/a' 
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, annex_2_xpath)))

        annex_2_link = driver.find_element(By.XPATH, annex_2_xpath).get_attribute('href')

        # faz o download do Anexo 2 para a pasta de download
        annex_2_path = current_path / "downloads/anexo_2.pdf"

        urllib.request.urlretrieve(annex_2_link, annex_2_path)

        # Compacta os arquivos baixados
        file_list = [annex_1_path, annex_2_path]
        zip_path = current_path / "results/anexos.zip"

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in file_list:
                zipf.write(file, arcname=Path(file).name)

        # Retorna o resultado
        print("Operação Concluida") 
        return zip_path

    except Exception as e:
        # Caputura e imprime o erro
        print("Operação Interrompida") 
        print(f"Erro: {e}")

        return None

result_file = download_files("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")
print(result_file)